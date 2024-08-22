from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.BlogPost], tags=['Blogs'])
def read_blog_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = crud.get_blog_posts(db, skip=skip, limit=limit)
    return blogs

@router.get("/{blog_post_id}", response_model=schemas.BlogPost, tags=['Blogs'])
def read_blog_post(blog_post_id: int, db: Session = Depends(get_db)):
    blog_post = crud.get_blog_post(db, blog_post_id=blog_post_id)
    if blog_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blog_post

@router.put("/{blog_post_id}", response_model=schemas.BlogPost, tags=['Blogs'])
def update_blog_post(blog_post_id: int, blog_post: schemas.BlogPostUpdate, db: Session = Depends(get_db)):
    db_blog_post = crud.get_blog_post(db, blog_post_id=blog_post_id)
    if db_blog_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    updated_blog = crud.update_blog_post(db=db, blog_post_id=blog_post_id, blog_post=blog_post)
    return updated_blog

@router.delete("/{blog_post_id}", response_model=schemas.BlogPost, tags=['Blogs'])
def delete_blog_post(blog_post_id: int, db: Session = Depends(get_db)):
    db_blog_post = crud.get_blog_post(db, blog_post_id=blog_post_id)
    if db_blog_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    crud.delete_blog_post(db=db, blog_post_id=blog_post_id)
    return db_blog_post
