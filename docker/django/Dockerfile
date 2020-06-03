###
# jhlee / 2018-05-11
# reference : http://ruddra.com/2016/08/14/docker-django-nginx-postgres/
###
FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_DEBUG 0
ENV DJANGO_ALLOWED_HOST "*"

RUN apt-get update && \
    apt-get install -y \
    python-dev \
    default-libmysqlclient-dev \
    net-tools \
    git \
	iputils-ping \
    vim \
    less \
    procps && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/junhwanLee/drf-oms.git /src 
RUN mkdir /config
RUN pip install -U pip
RUN pip install -r /src/requirements.txt && pip install gunicorn
RUN cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime

ENV homedir /src
WORKDIR /src

COPY ./entrypoint.sh /src/
RUN chmod +x /src/entrypoint.sh
ENTRYPOINT ./entrypoint.sh
