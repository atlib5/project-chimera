setup:
	pip install pytest

test:
	pytest

docker-test:
	docker build -t chimera-tests .
	docker run chimera-tests
