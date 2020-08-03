FROM gcr.io/kaggle-gpu-images/python:latest
RUN pip install --upgrade pip

WORKDIR /srv
COPY . .
RUN pip install -e .[dev]
