start:
	docker build -t filters .
	docker run -d --restart=always --name tamuctf-filters -p 80:80 filters
stop:
	docker container rm -f tamuctf-filters

