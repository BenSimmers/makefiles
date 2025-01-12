PROJECT_NAME = MyCSharpApp
OUTPUT_DIR = bin/Debug/net7.0
DOCKER_IMAGE_NAME = app
PORT = 5000

# Phony targets
.PHONY: run build clean test build-docker run-docker

run:
    dotnet run --project $(PROJECT_NAME)

build:
    dotnet build $(PROJECT_NAME)

clean:
    dotnet clean $(PROJECT_NAME)

test:
    dotnet test $(PROJECT_NAME)

build-docker:
    docker build -t $(DOCKER_IMAGE_NAME) .

run-docker:
    docker run -p $(PORT):$(PORT) $(DOCKER_IMAGE_NAME)