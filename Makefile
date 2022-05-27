.PHONY: test


test:
	docker-compose run --rm app pytest -p no:cacheprovider tests/