.DEFAULT_GOAL := help

help: ## Show this help message.
	@echo "Usage: make <target>"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

migrate: ## Run Django migrations.
	@echo "Running migrations..."
	python manage.py migrate

runserver: ## Start the Django development server.
	@echo "Starting the Django development server..."
	python manage.py runserver

run: migrate runserver ## Run migrations, collect static files, and start the server.

test-dev: ## Run Django tests in dev-mode
	@echo "Running tests..."
	python manage.py test

test-docker: ## Run Django tests.
	@echo "Running tests inside Docker container..."
	docker compose exec web python manage.py test
	
lint: ## Run linters.
	@echo "Running linters..."
	flake8 .
	black --check .
