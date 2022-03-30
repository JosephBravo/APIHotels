from typing import Optional
from pydantic import BaseModel


class Hotel(BaseModel):
    id: Optional[str]
    name: str
    city: str
    email: str
    url_picture: str
    date_created: str
