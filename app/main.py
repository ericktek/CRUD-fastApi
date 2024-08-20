from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.User, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User], tags=['Users'])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User, tags=['Users'])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/blogs/", response_model=schemas.BlogPost, tags=['Blogs'])
def create_blog_post_for_user(user_id: int, blog_post: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    return crud.create_blog_post(db=db, blog_post=blog_post, user_id=user_id)

@app.get("/blogs/", response_model=list[schemas.BlogPost], tags=['Blogs'])
def read_blog_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = crud.get_blog_posts(db, skip=skip, limit=limit)
    return blogs

@app.get("/blogs/{blog_post_id}", response_model=schemas.BlogPost, tags=['Blogs'])
def read_blog_post(blog_post_id: int, db: Session = Depends(get_db)):
    blog_post = crud.get_blog_post(db, blog_post_id=blog_post_id)
    if blog_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blog_post
