start:
	docker build -t agent .
	docker run --read-only -d --restart=always --name tamuctf-agent -p 9000:80 agent
stop:
	docker container rm -f tamuctf-agent

