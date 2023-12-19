from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, DateTime, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

# Create a base model
Base = declarative_base()

# Defining blog models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    phone = Column(VARCHAR, nullable=False, unique=True)

    # One-to-many relationship with blog posts
    posts = relationship("BlogPost", back_populates="author")

class BlogPost(Base):
    __tablename__ = "blog_posts"

    # Define columns
    id = Column(Integer(), primary_key=True)
    title = Column(Text(), nullable=False)
    category = Column(Text(), nullable=False)
    subCategory = Column(Text(), nullable=False)
    content = Column(Text(), nullable=False)
    author_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    createdAt = Column(TIMESTAMP)
    cover = Column(VARCHAR, nullable=False)

    # One-to-many relationship with comments
    comments = relationship("Comment", back_populates="blog_post")

    # Many-to-one relationship with users
    author = relationship("User", back_populates="posts")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer(), primary_key=True)
    comment_text = Column(Text(), nullable=False)

    # Foreign keys
    post_id = Column(Integer(), ForeignKey('blog_posts.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))

    # Many-to-one relationship with blog posts
    blog_post = relationship("BlogPost", back_populates="comments")

    # Many-to-one relationship with users
    user = relationship("User", back_populates="comments")
