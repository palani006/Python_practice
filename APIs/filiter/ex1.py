from fastapi import FastAPI,HTTPException
from typing import Optional

app = FastAPI()

expample=[
    {"id":1,"name":"ram","city":"kuppam"},
    {"id":2,"name":"raj","city":"hyd"},
    {"id":3,"name":"kaml","city":"blr"},
    {"id":4,"name":"ramu","city":"chnai"}
]

@app.get("/exa")
def get_exapmle(city: Optional[str]=None , limit:int =10):
    result=(expample)

    if city:
        result=[s for s in result if s["city"]==city]

    return result[:limit]