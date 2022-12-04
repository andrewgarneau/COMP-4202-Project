from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from geospatial_processing.geopython import get_nearest_repair_stand_json, get_route_to_nearest_repair_stand
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/repair-stand")
def get_repair_stand(x: Union[float,None], y: Union[float, None]):
    my_nearest = get_nearest_repair_stand_json(x, y)
    return {"data": my_nearest}

@app.get("/repair-stand-route")
def get_repair_stand(x: Union[float,None], y: Union[float, None]):
    print("In the routing for get_route_to_nearest_repair_stand")
    my_nearest = get_route_to_nearest_repair_stand(x, y)
    return {"data": my_nearest}