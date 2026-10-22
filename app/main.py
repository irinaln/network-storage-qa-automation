from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Network QA Lab")
items: dict[str, str] = {}

class Item(BaseModel):
    value: str

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.put('/items/{key}')
def put_item(key: str, item: Item):
    items[key] = item.value
    return {'key': key, 'value': item.value}

@app.get('/items/{key}')
def get_item(key: str):
    if key not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    return {'key': key, 'value': items[key]}
