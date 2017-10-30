FROM ubuntu:xenial

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates \
    python3-setuptools \
    python3-dev \
    build-essential \
    openjdk-8-jre-headless \
 && easy_install3 pip \
 && pip3 install -U --no-cache-dir pip \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
RUN pip3 install -U --no-cache-dir -r /requirements.txt \
 && python3 -m spacy download en

COPY examples /examples

ENV PYTHONIOENCODING=UTF-8

CMD /examples/basic/basic.py
