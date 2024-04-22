from typing import Optional
from fastapi import FastAPI, HTTPException
from model import BlogPost
from database import *

app = FastAPI()

@app.get('/')
def root():
    return {"Hello":"Blog"}

@app.get('/api/showall')
async def show():
    posts = await get_all()
    if posts:
        return posts
    raise HTTPException(404, "{'Error':'Not Found'}")

@app.get('/api/show/{title}', response_model=BlogPost)
async def show_by_title(title:str):
    response = await get_one_post(title)
    if response:
        return response
    raise HTTPException(404, f"There is no post with {title}")

@app.post('/api/addnew', response_model=BlogPost)
async def add_new(blogpost:BlogPost):
    response = await add_blog_post(blogpost.dict())
    if response:
        return response
    raise HTTPException(400, f"Bad request")

@app.put('/api/change{title}', response_model=BlogPost)
async def change(title:str, desc:str, auth:str, timeRead:Optional[int]):
    response = await update(title, desc, auth, timeRead)
    if response:
        return response
    raise HTTPException(404, f"There is no post with {title}")

@app.delete('/api/delete{title}')
async def delete(title:str):
    response = await delete_post(title)
    if response:
        return response
    raise HTTPException(404, f"There is no post with {title}")