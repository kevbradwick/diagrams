.PHONT: fmt
fmt:
	poetry run isort .
	poetry run black .