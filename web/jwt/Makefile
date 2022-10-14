NAME := jwt
PORT := 9005


make run:
	docker build . -t $(NAME)
	docker run -d --read-only --restart=always --name $(NAME) -p $(PORT):5004 $(NAME)

