## HotelsHotels

## Requirements 🔧

* [flask](https://flask.palletsprojects.com/en/2.1.x/)
* [pydantic](https://pydantic-docs.helpmanual.io/)
* [fastapi](https://fastapi.tiangolo.com/)
* [starlette](https://www.starlette.io/)
* [pymongo](https://www.mongodb.com/cloud/atlas/lp/try2?adgroup=131761122172)
* [pytest](https://docs.pytest.org/en/7.1.x/)
* [urllib3](https://pypi.org/project/urllib3/)

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
