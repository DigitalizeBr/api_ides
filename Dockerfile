# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
WORKDIR /usr/src/ides
RUN mkdir -p /usr/src/app/images
VOLUME /usr/src/app/images


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc tesseract-ocr \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .