from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

food =[
    {"id":7,"name":"poori","table":"fifth"},
    {"id":8,"name":"dosa","table":"sixth"},
    {"id":9,"name":"idle","table":"seventh"}
]

f_id=10


class resturent(BaseModel):
    name:str
    table:str

@app.get("/")
def read():
    return food

@app.post("/add_new",status_code=201)
def add_new_food(f : resturent):
    global f_id
    new_food={
        "id":f_id,
        "name":f.name,
        "table":f.table
    }
    
    food.append(new_food)
    f_id+=1
    return new_food

@app.put("/update")
def update(a_id: int ,palani:resturent ):
    for i, f1 in enumerate(food):
        if f1["id"] == a_id:
            food[i]={
                "id":f_id,
                "name":a_id.name,
                "tablel":a_id.table
            }
            return food
        raise HTTPException(status_code=404, detail=f"food with id {a_id} not found")

@app.delete("/delete")
def delete_item(a_id: int):
    for i,s2 in enumerate(a_id):
        if s2["id"] == a_id:
            delete=food.pop(i)
            return {"delete"}
        raise HTTPException(status_code=404, detail=f"food with {a_id} not found")