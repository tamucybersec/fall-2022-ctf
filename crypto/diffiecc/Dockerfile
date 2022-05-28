FROM python:slim-buster

RUN apt-get update -y; apt-get install socat -y

COPY flag.txt /crypto/flag.txt
COPY chall.py /crypto/chall.py
RUN chmod +x /crypto/chall.py
RUN python3 -m pip install pycryptodome
WORKDIR /crypto
EXPOSE 7077

RUN echo "exec socat -s TCP-LISTEN:7077,reuseaddr,fork EXEC:\"python3 /crypto/chall.py\",stderr" > /crypto/docker_entrypoint.sh

ENTRYPOINT ["sh", "/crypto/docker_entrypoint.sh"]
