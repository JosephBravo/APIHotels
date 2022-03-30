from fastapi import FastAPI
from routes.hotel import app
from docs import tags_metadata


api = FastAPI(
    title="API Hotels - Flask & Mongo",
    description="This is a REST API",
    version="0.0.1",
    openapi_tags=tags_metadata
)


api.include_router(app)
