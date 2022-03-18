FROM ghcr.io/bballiance/miaogram:v1.3.0

COPY *.py /miaogram/extra/

ENTRYPOINT ["/usr/local/bin/python3", "-u", "main.py"]
