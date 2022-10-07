start:
	docker build -t oncampus .
	docker run -d --restart=always --name tamuctf-oncampus -p 1337:1337 oncampus
stop:
	docker container rm -f tamuctf-oncampus
