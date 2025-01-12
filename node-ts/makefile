# Variables
ENTRYPOINT = src/index.ts
OUTPUT_DIR = dist
IMAGE_NAME = ts-app
PORT = 3000

.PHONY: run watch build clean build-docker run-docker test

run:
    ts-node $(ENTRYPOINT)

watch:
    nodemon --exec ts-node $(ENTRYPOINT)

test:
    npm test

build:
    tsc

clean:
    rm -rf $(OUTPUT_DIR)

# Docker commands
build-docker:
    docker build -t $(IMAGE_NAME) .

run-docker:
    docker run -p $(PORT):$(PORT) $(IMAGE_NAME)