from typing import Optional
from pydantic import BaseModel

class BlogPost(BaseModel):
    title:str
    description:str
    author:str
    readTime:Optional[int]