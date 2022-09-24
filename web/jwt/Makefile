NAME := jwt
PORT := 7000


make run:
	docker build . -t $(NAME)
	docker run -d --read-only --restart=always --name $(NAME) -p $(PORT):5004 $(NAME)

