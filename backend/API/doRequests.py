from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    country: str
    date: str

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
