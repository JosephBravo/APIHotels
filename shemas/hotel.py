

def hotel_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "city": item["city"],
        "address": item["address"],
        "email": item["email"],
        "url_picture": item["url_picture"],
        "date_created": item["date_created"]
    }


def hotels_entity(entity) -> list:
    return [hotel_entity(item) for item in entity]

# def serializeDict(a) -> dict:
#     return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}
