FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  && apt-get install -y build-essential procps telnet curl unzip wget xvfb tar bzip2 libgtk-3-0 libdbus-glib-1-2 \
  && apt-get install -y python3-dev default-libmysqlclient-dev build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext 

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

RUN mkdir /app
RUN mkdir /app/staticfiles
RUN mkdir /app/mediafiles

WORKDIR /app/src

COPY ./src .

ENTRYPOINT ["/entrypoint"]
