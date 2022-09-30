FROM python:3.8-slim-buster
COPY src/ /

RUN apt update -y && apt upgrade -y && pip3 install flask

ENTRYPOINT ["python3", "app.py"]
