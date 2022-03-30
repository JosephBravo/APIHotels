from fastapi import FastAPI
from routes.hotel import api
from docs import tags_metadata


app = FastAPI(
    title="API Hotels - Flask & Mongo",
    description="This is a REST API",
    version="0.0.1",
    openapi_tags=tags_metadata
)


app.include_router(api)
