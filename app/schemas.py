from pydantic import BaseModel

class BlogPostBase(BaseModel):
    title: str
    description: str
    image: str

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    blogs: list[BlogPost] = []

    class Config:
        orm_mode = True
