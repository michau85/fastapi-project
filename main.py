from fastapi import FastAPI,Path
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    age:int


inv=[]
app=FastAPI()
@app.get('/')
def home():
    return {"data":"Tet"}

@app.get('/about')
def about():
    return 'about'

@app.post('/create-item')
def create_item(item:Item):
    numer=len(inv)+1
    inv[]=item

@app.get('/items')
def items():
    return inv


@app.get('/item/{id}')
def gi(id:int=Path(None,description="Iden produktu")):
    return inv[id]

@app.get('/byname')
def by(name:str=None):
    return 'byname'

    return numer
