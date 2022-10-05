FROM alpine/socat

COPY quiz.sh /quiz.sh
RUN chmod +x /quiz.sh ; echo "exec socat -s TCP-LISTEN:1337,reuseaddr,fork EXEC:/quiz.sh,stderr" > /docker_entrypoint.sh

ENTRYPOINT ["sh", "/docker_entrypoint.sh"]
