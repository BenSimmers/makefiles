CONTAINER_PROVIDER = docker
ENTRYPOINT = index.ts
OUTPUT_DIR = dist
IMAGE_NAME = bun-api-server
PORT = 8080

# Phony targets
.PHONY: run watch bun-build clean build-docker run-docker test

run:
	bun $(ENTRYPOINT)

watch:
	bun --watch --hot $(ENTRYPOINT)

test:
	bun test

bun-build:
	bun build --entrypoints ./$ENTRYPOINT --outdir ./$OUTPUT_DIR

clean:
	rm -rf $(OUTPUT_DIR)

# Docker commands
build-docker:
	$(CONTAINER_PROVIDER) build -t $(IMAGE_NAME) .

run-docker:
	$(CONTAINER_PROVIDER) run -p $(PORT):$(PORT) $(IMAGE_NAME)