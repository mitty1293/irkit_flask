FROM python:3

COPY requirements.txt /tmp

RUN pip3 install --upgrade pip && \
    pip3 install -r /tmp/requirements.txt

