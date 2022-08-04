NAME := echo_jail
PORT := 7000

docker: Dockerfile
	docker build -t $(NAME) --build-arg name=$(NAME) --build-arg port=$(PORT) .

run: docker
	docker run -d --read-only --restart=always --name $(NAME) -p $(PORT):$(PORT) $(NAME)

clean:
	docker stop $(NAME) && docker rm $(NAME) && docker rmi $(NAME)
