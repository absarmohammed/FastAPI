from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from model import BlogPost

client = AsyncIOMotorClient("mongodb://localhost:27017")
database = client.Blog
collection = database.blogPosts

async def add_blog_post(blogpost:BlogPost):
    await collection.insert_one(blogpost)
    return blogpost

async def get_one_post(title:str):
    blogpost = await collection.find_one({"title":title})
    return blogpost

async def get_all():
    posts = []
    all = collection.find({})
    async for i in all:
        posts.append(BlogPost(**(i)))
    return posts

async def update(title:str, desc:str, auth:str, timeRead:Optional[int]):
    if not timeRead:
        timeRead = collection.find_one({"title":title}).dict()[timeRead]
    await collection.update_one({"title":title}, {"$set":{"description":desc, "author":auth, "readTime":timeRead}})
    post = await collection.find_one({"title":title})
    return post

async def delete_post(title:str):
    if await get_one_post(title):
        await collection.delete_one({"title":title})
        return True
    else:
        return False