
SHELL = /bin/bash
.SHELLFLAGS = -o pipefail -c

.PHONY: help
help: ## Print info about all commands
	@echo "Helper Commands:"
	@echo
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "    \033[01;32m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build the project
	pnpm build

.PHONY: start
start: ## Start the project
	pnpm run dev


.PHONY: lint
lint: ## Lint the project
	pnpm verify

.PHONY: fmt
fmt: ## Format the project
	pnpm format

.PHONY: deps
deps: ## Install dependencies
	pnpm install --frozen-lockfile

.PHONY: nvm-setup
nvm-setup: ## Setup nvm
	nvm install 18
	nvm use 18
	corepack enable
