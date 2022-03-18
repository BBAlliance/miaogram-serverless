import asyncio
from controllers.base import onSchedule, onCommand, every, Context, Args
from pyrogram import Client
from pyrogram.types import Message
from os import system, environ
from utils.utils import existDataFile
from utils.logger import info

APK = "curl"

@onCommand("backup", minVer="1.3.0", help="backup: 使用 MIAOSS 的备份服务")
async def handler(args: Args, client: Client, msg: Message, ctx: Context):
    await msg.edit("备份中...")
    if task():
        await msg.edit("备份成功 ~")
    else:
        await msg.edit("出错啦...")
    
    await asyncio.sleep(5)
    await msg.delete()

@onSchedule(every(15).minutes)
def task() -> bool:
    if "MIAOSS" in environ and existDataFile("miaogram.session"):
        endpoint = environ["MIAOSS"]
        code = system("""bash -c 'cd /miaogram/data && tar zcf /miaoss.tgz . --exclude=".git" --exclude="__pycache__" --exclude="downloads" --exclude="miaogram.session-journal"'""")
        if code == 0:
            code = system(f"""bash -c 'curl -XPOST --data-binary @/miaoss.tgz {endpoint}'""")
        if code == 0:
            code = system(f"""bash -c 'rm -rf /miaoss.tgz'""")
            info("Backup Service: success")
            return True
        info("Backup Service: failure")
    else:
        info("Backup Service: skipped")
    return False
