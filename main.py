# Import necessary modules and classes from FastAPI, SQLAlchemy, and other files
from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import BlogPost, User, Comment  # Importing models from models.py
from schemas import BlogPostCreate, BlogPostResponse  # Importing schemas from schemas.py


# Create a FastAPI instance
app = FastAPI()

# Configure CORS settings
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define route to get all blog posts
@app.get('/blog-posts')
def blog_posts(db: Session = Depends(get_db)):
    return db.query(BlogPost).all()

# Define route to get a specific blog post by ID
@app.get('/blog-posts/{post_id}')
def blog_post(post_id: int, db: Session = Depends(get_db)):
    blog_post = db.query(BlogPost).filter(BlogPost.id == post_id).first()

    # Raise HTTPException if the blog post is not found
    if blog_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog post {post_id} not found")

    return blog_post

# Define route to create a new blog post
@app.post('/blog-posts')
def create_blog_post(post: BlogPostCreate, db: Session = Depends(get_db)):
    new_post = BlogPost(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": "Blog post created successfully", "blog_post": new_post}

# Define route to update an existing blog post by ID
@app.patch('/blog-posts/{post_id}')
def update_blog_post(post_id: int, post: BlogPostCreate, db: Session = Depends(get_db)):
    updated_post = db.query(BlogPost).filter(BlogPost.id == post_id).first()

    # Update the blog post if it exists
    if updated_post:
        for key, value in post.dict().items():
            setattr(updated_post, key, value)

        db.commit()
        db.refresh(updated_post)
        return {"message": f"Blog post {post_id} updated successfully", "blog_post": updated_post}

    # Raise HTTPException if the blog post is not found
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog post {post_id} not found")

# Define route to delete a blog post by ID
@app.delete('/blog-posts/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_post(post_id: int, db: Session = Depends(get_db)):
    deleted_post = db.query(BlogPost).filter(BlogPost.id == post_id).first()

    # Delete the blog post if it exists
    if deleted_post:
        db.delete(deleted_post)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    # Raise HTTPException if the blog post is not found
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog post {post_id} not found")
