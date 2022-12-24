FROM python:3

WORKDIR /usr/src/app

RUN pip install aiogram
RUN pip install http3
RUN pip install asyncio
RUN pip install lorem

COPY main.py /usr/src/app