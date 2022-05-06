from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel, Field


class Job(BaseModel):
    uid: str = Field(..., example="123")
    message: str
    variables: List[Dict[str, str]]
    paper_type: str
    paper_size: str
    paper_orientation: str

    class Config:
        schema_extra = {
            "example": {
                "uid": "123",
                "message": "Dear {name}, thank-you for buying {product}",
                "variables": [
                        {"name": "joe", "product": "t-shirt"},
                        {"name": "alice", "product": "trowsers"},
                    ],
                "paper_type": "pt1",
                "paper_size": "a6",
                "paper_orientation": "landscape",
            }
        }

app = FastAPI()


# demo
@app.get("/")
def read_root():
    return {"Hello": "World"}


# https://fastapi.tiangolo.com/tutorial/body/
@app.post("/api/v1/create/")
async def create_item(job: Job):
    # add_to_que(item)
    return job

