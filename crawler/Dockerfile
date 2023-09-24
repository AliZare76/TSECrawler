FROM python:latest

COPY ./crawler .

RUN apt-get install libpq-dev

RUN pip3 install -r requirements.txt

RUN python3 crawler.py