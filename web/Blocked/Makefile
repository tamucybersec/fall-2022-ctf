run:
	docker build -t blocked .
	docker run -d --restart=always --name tamuctf-blocked -p 80:80 blocked
stop:
	docker container rm -f tamuctf-blocked

