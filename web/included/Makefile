start:
	docker build -t included .
	docker run -d --restart=always --name tamuctf-included -p 80:80 included
stop:
	docker container rm -f tamuctf-included

