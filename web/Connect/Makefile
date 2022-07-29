run:
	docker build --no-cache -t connect .
	docker run --read-only -d --restart=always --name tamuctf-connect -p 80:80 connect
stop:
	docker container rm -f tamuctf-connect
