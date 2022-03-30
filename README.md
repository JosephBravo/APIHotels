HotelsHotels

Requirements 🎯
flask
pydantic
fastapi
starlette
pymongo
pytest
urllib3

Installation [Linux] 
Clone repository and create virtual environment in project folder:

_python3 -m venv somename_

Activate environment:

_. venv/bin/activate_

Install requirements:

pip install -e .

Execution - Run Project [Linux] 🚀
Located in project rest_api run command:

_uvicorn app:app --port 8089 --reload_

This will run the application on port http://127.0.0.1:8089

Documentation [SwaggerUI]📋
After running the project ...
URL documentation: http://127.0.0.1:8089/docs#/

Run Test [Pytest]
Located in project rest_api run command:

_pytest_
