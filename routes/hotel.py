# Api
from fastapi import APIRouter, status, Response
from starlette.status import HTTP_204_NO_CONTENT

# Models - database - entity's
from models.hotel import Hotel
from config.db import conn
from shemas.hotel import hotel_entity, hotels_entity

# Utils
from bson import ObjectId
from src.utils import is_valid_email

hotel = APIRouter()


@hotel.get('/hotels')
async def find_all_hotel():

    return hotels_entity(conn.local.hotel.find())


@hotel.post('/create_hotel', response_model=Hotel, tags=["create_hotel"])
async def create_hotel(hotel: Hotel):
    new_hotel = dict(hotel)
    print(new_hotel['email'])
    valid = is_valid_email(new_hotel['email'])
    if not valid:
        print("EMAIL NO VALIDO MEN")
    del new_hotel['id']
    id = conn.local.hotel.insert_one(new_hotel).inserted_id
    print("ID/", id)
    hotel = conn.local.hotel.find_one({"_id": id})
    return hotel_entity(hotel)


@hotel.get('/hotels/{id}', response_model=Hotel, tags=["retrieve_hotel"])
async def retrieve_user(id: str):
    return hotel_entity(conn.local.hotel.find_one({"_id": ObjectId(id)}))


@hotel.put('/hotels/{id}', response_model=Hotel, tags=["update_hotel"])
async def update_user(id: str, hotel: Hotel):
    conn.local.hotel.find_one_and_update({"_id": ObjectId(id)},
                                         {"$set": dict(hotel)})
    return hotel_entity(conn.local.hotel.find_one({"_id": ObjectId(id)}))


@hotel.delete("/hotels/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["delete_hotel"])
async def delete_user(id: str):
    conn.local.hotel.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)

# @hotel.errorhandler(404)
# def not_found(error=None):
#     message = {
#         'message': 'Resource Not Found ' + request.url,
#         'status': 404
#     }
#     response = jsonify(message)
#     response.status_code = 404
#     return response
