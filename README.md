
# ETL - Project


## API Reference

#### Get all analyst

```http
  GET /api/analyst
```

#### Get analyst

```http
  GET /api/analyst/${name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Id of analyst to fetch |


#### Post analyst

```http
  POST /api/analyst/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.     |
| `is_admin`      | `string` | **Required**.     |


#### Delete analyst

```http
  DELETE /api/analyst/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.     |




## Documentation

[FastAPI](https://fastapi.tiangolo.com)
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

[Pandas](https://pandas.pydata.org)
pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.

[Uvicorn](https://www.uvicorn.org)
Uvicorn is an ASGI web server implementation for Python.
Until recently Python has lacked a minimal low-level server/application interface for async frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all async frameworks.

[Swagger](https://swagger.io/)
Simplify API development for users, teams, and enterprises with the Swagger open source and professional toolset. Find out how Swagger can help you design and document your APIs at scale.
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DATABASE_URL`=postgresql://admin:12345@127.0.0.1:5455/{table_name}

`FILE_XLS`

`SHEET_NAME`

`TABLE_NAME`



## Deployment

Run database

```bash
  docker run --name django_db -p 5456:5432 -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=12345 -e POSTGRES_DB=postgres -d postgres

```


## Installation

Initialize project

```bash
    virtualenv -p python3 env
    source venv/bin/activate
    pip install -r requirements.txt
    python etl.py
```


Run RESTAPI

```bash
    uvicorn sql_app.main:app --reload
```
