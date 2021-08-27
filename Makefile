isort:
	isort ./fastapi_users_db_ormar ./tests

format: isort
	black .

test:
	pytest --cov=fastapi_users_db_ormar/ --cov-report=term-missing --cov-fail-under=100

bumpversion-major:
	bumpversion major

bumpversion-minor:
	bumpversion minor

bumpversion-patch:
	bumpversion patch
