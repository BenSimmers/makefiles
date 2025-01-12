# Variables
ENTRYPOINT = index.js
OUTPUT_DIR = dist
IMAGE_NAME = node-app
PORT = 3000

.PHONY: run watch build clean build-docker run-docker test

run:
    node $(ENTRYPOINT)

watch:
    nodemon $(ENTRYPOINT)

test:
    npm test

build:
    npm run build

clean:
    rm -rf $(OUTPUT_DIR)

build-docker:
    docker build -t $(IMAGE_NAME) .

run-docker:
    docker run -p $(PORT):$(PORT) $(IMAGE_NAME)