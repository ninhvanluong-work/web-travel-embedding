# Makefile for deploying the application

.PHONY: all build run stop pull login

# Default target
all:
	@$(MAKE) build
	@$(MAKE) run

login:
	ssh ec2-user@ec2-3-86-229-179.compute-1.amazonaws.com

pull:
	git pull origin main

build:
	docker build -t web-travel-embedding -f Dockerfile.prod .

stop:
	$(eval CONTAINER_ID := $(shell sudo docker ps -q --filter publish=80))
	@if [ ! -z "$(CONTAINER_ID)" ]; then \
		echo "Stopping and removing container $(CONTAINER_ID)"; \
		sudo docker stop $(CONTAINER_ID); \
		sudo docker rm $(CONTAINER_ID); \
	fi

run: stop
	sudo docker run -d -p 80:8000 web-travel-embedding
