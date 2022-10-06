NAME := pwn2004

build:
	docker build -t $(NAME) . 
run: build
	docker run --name $(NAME) -it $(NAME)
clean:
	docker container rm -f $(NAME)
dist:
	$(eval id := $(shell docker create $(NAME)))
	docker cp $(id):/core .
	docker cp $(id):/treasure-hunt .
	docker rm -v $(id)
	zip -r treasure-hunt.zip ./treasure-hunt.c ./treasure-hunt ./core
