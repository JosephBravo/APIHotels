## HotelsHotels

## Requirements 🔧
flask
pydantic
fastapi
starlette
pymongo
pytest
urllib3

## Installation 📌

Clone repository and create virtual environment in project folder:

```
python3 -m venv somename
```

## Activate environment: ▶️

```
. venv/bin/activate
```

## Install requirements: 🎯

```
pip install -e .
```

## Execution - Run Project [Linux] 🚀

Located in project rest_api run command:

```
uvicorn app:app --port 8089 --reload
```

This will run the application on port http://127.0.0.1:8089

## Documentation [SwaggerUI]📋

After running the project ...
URL documentation: http://127.0.0.1:8089/docs#/

## Run Test [Pytest] 🔍

Located in project rest_api run command:

```
pytest
```
