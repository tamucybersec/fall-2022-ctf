run:
	docker build --no-cache -t blocked-out .
	docker run --read-only -d --restart=always --name tamuctf-blocked-out -p 8888:8888 blocked-out
stop:
	docker container rm -f tamuctf-blocked-out && docker rmi blocked-out

