FROM continuumio/miniconda3

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH "/llama"
ENV RANK 1
ENV WORLD_SIZE 1
ENV MASTER_ADDR 172.19.0.2 
ENV MASTER_PORT 7777
ENV LOGLEVEL="DEBUG"
