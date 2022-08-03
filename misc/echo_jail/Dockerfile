FROM python:slim-buster

RUN apt-get update -y; apt-get install socat -y

ARG port

COPY jail.py /jail.py
COPY flag.txt /flag.txt
RUN chmod +x jail.py
WORKDIR /
EXPOSE $port

RUN echo "exec socat -s TCP-LISTEN:$port,reuseaddr,fork EXEC:\"python3 /jail.py\",stderr" > /docker_entrypoint.sh

ENTRYPOINT ["sh", "/docker_entrypoint.sh"]
