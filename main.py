from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, joinedload
from database import get_db
from models import BlogPost
from schemas import BlogPostCreate, BlogPostResponse

# Initialize the FastAPI app
app = FastAPI()

# CORS settings
origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

# Route to get all blog posts
@app.get('/blog-posts')
def blog_posts(db: Session = Depends(get_db)):
    blog_posts = db.query(BlogPost).all()
    return blog_posts

# Route to get a single blog post by ID
@app.get('/blog-posts/{post_id}')
def blog_post(post_id: int, db: Session = Depends(get_db)):
    blog_post = db.query(BlogPost).filter(BlogPost.id == post_id).first()

    return blog_post

# Route to create a new blog post
@app.post('/blog-posts')
def create_blog_post(post: BlogPostCreate, db: Session = Depends(get_db)):
    new_post = BlogPost(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": "Blog post created successfully", "blog_post": new_post}

# Route to update a blog post by ID
@app.patch('/blog-posts/{post_id}')
def update_blog_post(post_id: int, post: BlogPostCreate, db: Session = Depends(get_db)):
    updated_post = db.query(BlogPost).filter(BlogPost.id == post_id).first()

    if updated_post:
        for key, value in post.dict().items():
            setattr(updated_post, key, value)

        db.commit()
        db.refresh(updated_post)
        return {"message": f"Blog post {post_id} updated successfully", "updated_post": updated_post}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog post {post_id} not found")

# Route to delete a blog post by ID
@app.delete('/blog-posts/{post_id}')
def delete_blog_post(post_id: int, db: Session = Depends(get_db)):
    deleted_post = db.query(BlogPost).filter(BlogPost.id == post_id).first()

    if deleted_post:
        db.delete(deleted_post)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog post {post_id} not found")
