NAME := treasure-hunt

build:
	docker build -t $(NAME) . 
run: build
	docker run --privileged --name $(NAME) -it $(NAME)
clean:
	docker container rm -f $(NAME)
dist: build
	$(eval id := $(shell docker create --privileged $(NAME)))
	docker cp $(id):/core .
	docker cp $(id):/treasure-hunt .
	docker rm -v $(id)
	zip -r treasure-hunt.zip ./treasure-hunt.c ./treasure-hunt ./core
