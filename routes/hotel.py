# Api
from fastapi import APIRouter, status, Response
from flask import Flask
from starlette.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT

# Models - database - entity's
from models.hotel import Hotel
from config.db import conn
from shemas.hotel import hotel_entity, hotels_entity

# Utils
from bson import ObjectId
from src.utils import *
from datetime import datetime

api = APIRouter()
flask = Flask(__name__)


@api.get('/hotels')
async def find_all_hotel():
    return hotels_entity(conn.local.hotel.find())


@api.post('/create_hotel', response_model=Hotel, tags=["create_hotel"])
async def create_hotel(hotel: Hotel):
    new_hotel = dict(hotel)

    valid_email = is_valid_email(new_hotel['email'])
    if not valid_email:
        return exception_control("email", f'incorrect format email {new_hotel["email"]}')
    valid_name = valid_string(new_hotel['name'])
    if not valid_name:
        return exception_control("name", f'incorrect format name {new_hotel["name"]}. must not have numbers')
    valid_city = valid_string(new_hotel['city'])
    if not valid_city:
        return exception_control("city", f'incorrect format city {new_hotel["city"]}. must not have numbers')
    valid_url = validated_url(new_hotel['url_picture'])
    if not valid_url:
        return exception_control("url_picture", f'incorrect format url picture {new_hotel["url_picture"]}.')

    # add date of creation
    new_hotel["date_created"] = str(datetime.today())
    del new_hotel['id']
    _id = conn.local.hotel.insert_one(new_hotel).inserted_id
    hotel = conn.local.hotel.find_one({"_id": _id})
    return hotel_entity(hotel)


@api.get('/hotels/{id}', response_model=Hotel, tags=["retrieve_hotel"])
async def retrieve_user(id: str):
    return hotel_entity(conn.local.hotel.find_one({"_id": ObjectId(id)}))


@api.put('/hotels/{id}', response_model=Hotel, tags=["update_hotel"])
async def update_user(id: str, hotel: Hotel):
    conn.local.hotel.find_one_and_update({"_id": ObjectId(id)},
                                         {"$set": dict(hotel)})
    return hotel_entity(conn.local.hotel.find_one({"_id": ObjectId(id)}))


@api.delete("/hotels/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["delete_hotel"])
async def delete_user(id: str):
    conn.local.hotel.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)


def exception_control(field, err):
    return JSONResponse({field: err}, status_code=400)
