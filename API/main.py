from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel
from typing import Union
import pickle
from fastapi.middleware.cors import CORSMiddleware

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

# For iris classifier
class Iris(BaseModel):
    sepal_length : float
    sepal_width : float 
    petal_length : float
    petal_width : float

# loading in the model to predict on the data

pickle_in = open('model/classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
def predict_iris(iris:Iris):

    type = ""

    if(not(iris)):
        raise HTTPException(status_code=400, 
                            detail = "Please Provide a valid number")
    
    iris_dict = iris.dict()
    prediction = classifier.predict([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])

    if(prediction[0] == 0):
        type = "Iris-setosa"

    elif(prediction[0] == 1):
        type = "Iris-versicolor"
    
    elif(prediction[0] == 2):
        type = "Iris-virginica"
        
    return {
            "iris_type": type
           }
