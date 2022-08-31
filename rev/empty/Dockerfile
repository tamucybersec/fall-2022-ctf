FROM ubuntu:20.04

ARG name

RUN apt-get update -y; apt-get install build-essential -y
ADD $name.c /tmp/$name.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make all

