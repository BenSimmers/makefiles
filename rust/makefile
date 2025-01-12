BINARY_NAME=BinaryNameHERE

all: build

build:
	cargo build --release

run: build
	./target/release/$(BINARY_NAME)

install: build
	sudo cp ./target/release/$(BINARY_NAME) /usr/local/bin/$(BINARY_NAME)

clean:
	cargo clean

fmt:
	cargo fmt

check:
	cargo check

test:
	cargo test

.PHONY: all build run install clean fmt check test