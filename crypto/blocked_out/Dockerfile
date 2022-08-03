FROM python:slim-buster

RUN apt-get update -y; apt-get install socat -y

COPY flag.bmp /crypto/flag.bmp
COPY reveille.bmp /crypto/reveille.bmp
COPY picture1.bmp /crypto/picture1.bmp
COPY secrets.bmp /crypto/secrets.bmp
COPY chall.py /crypto/chall.py
RUN chmod +x /crypto/chall.py
RUN python3 -m pip install pycryptodome 
WORKDIR /crypto
EXPOSE 8888

RUN echo "exec socat -s TCP-LISTEN:8888,reuseaddr,fork EXEC:\"python3 /crypto/chall.py\",stderr" > /crypto/docker_entrypoint.sh

ENTRYPOINT ["sh", "/crypto/docker_entrypoint.sh"]
