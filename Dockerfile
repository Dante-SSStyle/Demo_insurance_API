#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
FROM python:3.10

COPY / /
WORKDIR /
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
