FROM python:3.6-alpine

RUN adduser -D flask_webapp

WORKDIR /home/flask_webapp

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY flask_webapp.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP flask_webapp.py

RUN chown -R flask_webapp:flask_webapp ./
USER flask_webapp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
