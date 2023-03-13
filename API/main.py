from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel
from typing import Union

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello World"}

# Path parameter
@app.get("/items/{item_id}")
def read_item(item_id:int):
    return {"item_id" : "This is response for "+str(item_id)}

# Query Parameter
@app.get("/items/query/{item_id}")
def read_query_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Class as input 
class ModelName(str, Enum):
    alexnet = "alexnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message":"Deep Learning FTW!"}
    if model_name == "lenet":
        return {"model_name": model_name, "message":"LeCBB all the images"}
    return {"model_name": model_name, "message": "others"}

# Request body
class Item(BaseModel):
    name : str
    description : Union[str, None] = None #default None
    price : float
    tax : Union[float, None] = None #default None

@app.post("/items/")
def create_item(item:Item):
    return item

@app.post("/items/update")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax: 
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Handling error
items = {"foo": "The Foo Wrestlers"}

@app.get("/items/handle/{item_id}")
def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

