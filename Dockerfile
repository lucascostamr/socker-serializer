FROM python:3.12-slim
WORKDIR /app
RUN apt-get upgrade &&\
    apt-get -y update
CMD sh