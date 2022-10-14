start:
	docker build -t included .
	docker run -d --restart=always --name tamuctf-included -p 9004:80 included
stop:
	docker container rm -f tamuctf-included

