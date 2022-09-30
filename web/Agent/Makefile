start:
	docker build -t agent .
	docker run --read-only -d --restart=always --name tamuctf-agent -p 8000:8000 agent
stop:
	docker container rm -f tamuctf-agent

