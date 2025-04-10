To run app:
```
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
# create .env file with your actual pass for DB (example in repo)

# to create fake data in DB
poetry run python -m goit_pythonweb_hw_06.seed

# to show required results
poetry run python -m goit_pythonweb_hw_06.my_select
```