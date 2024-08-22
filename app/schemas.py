from pydantic import BaseModel

# BlogPost Schemas
class BlogPostBase(BaseModel):
    title: str
    description: str
    image: str

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostUpdate(BlogPostBase):
    title: str | None = None
    description: str | None = None
    image: str | None = None

class BlogPost(BlogPostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

# User Schemas
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None

class User(UserBase):
    id: int
    blogs: list[BlogPost] = []

    class Config:
        orm_mode = True
