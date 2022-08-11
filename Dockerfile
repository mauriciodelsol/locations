FROM  --platform=linux/amd64 python:3.9-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add git
RUN apk update && apk add git

# add dependencies
RUN apk add python3-dev gcc g++ \ 
    && apk add --no-cache mariadb-dev
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

# install dependencies
RUN pip install --upgrade pip
RUN pip install mysqlclient
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
