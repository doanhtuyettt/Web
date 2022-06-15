# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN python3 -m pip install --upgrade pip
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
