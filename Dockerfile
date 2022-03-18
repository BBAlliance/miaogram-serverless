FROM ghcr.io/bballiance/miaogram

COPY *.py /miaogram/extra/

ENTRYPOINT ["/usr/local/bin/python3", "-u", "main.py"]
