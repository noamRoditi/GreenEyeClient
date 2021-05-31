# syntax=docker/dockerfile:1

FROM python:3.9.5-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENTRYPOINT ["python3","./k_mean_client.py"]