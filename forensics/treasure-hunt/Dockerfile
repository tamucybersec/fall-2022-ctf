FROM ubuntu:20.04
RUN apt-get update -y && apt-get install build-essential -y
COPY ./treasure-hunt.c ./flag.txt ./
RUN gcc -g treasure-hunt.c -o treasure-hunt -static
RUN echo  $(./treasure-hunt)
