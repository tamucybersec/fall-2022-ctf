FROM python:3.8-slim-buster

RUN apt update && apt upgrade && apt install -y curl && pip3 install flask && pip3 install mysql-connector-python
RUN mkdir /var/www

ENTRYPOINT ["python3", "/var/www/app.py"]
