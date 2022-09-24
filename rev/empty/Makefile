CC := $(or $(CC),gcc)
CFLAGS := -masm=intel
NAME := empty
PORT := 7000
all: $(NAME)

clean:
	rm -f $(NAME)

$(NAME): $(NAME).c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile $(NAME)
	docker build -t $(NAME) --build-arg name=$(NAME) .

run: docker
	docker run -d --read-only --restart=always --name $(NAME) $(NAME)

extract: docker
	$(eval id := $(shell docker create $(NAME)))
	docker cp $(id):/tmp/$(NAME) - | tar xv $(NAME)
	docker rm -v $(id)

dist: extract
	zip $(NAME).zip $(NAME)
