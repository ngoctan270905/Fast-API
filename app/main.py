from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

class ItemOut(BaseModel):
    name: str
    price: float

# @app.post("/items/", response_model=ItemOut)
# async def create_item(item: Item):
#     # dù item có description, client chỉ nhận name + price
#     return item

from fastapi import status

@app.post("/items/", response_model=ItemOut)
async def create_item(item: Item):
    return item
