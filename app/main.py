from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    uid: str
    message: str
    variables: List[Dict[str, str]]
    paper_type: str
    paper_size: str
    paper_orientation: str


app = FastAPI()


# demo
@app.get("/")
def read_root():
    return {"Hello": "World"}


# https://fastapi.tiangolo.com/tutorial/body/
@app.post("/api/v1/create/")
async def create_item(item: Item):
    return item
