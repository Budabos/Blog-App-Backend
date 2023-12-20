# Import necessary modules and classes from SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

# Create a base model
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "users"

    # Define columns
    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    phone = Column(VARCHAR, nullable=False, unique=True)

    # Define one-to-many relationship with blog posts and comments
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="user")

# Define the BlogPost model
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

    # Define one-to-many relationship with comments and many-to-one relationship with users
    comments = relationship("Comment", back_populates="blog_post")
    author = relationship("User", back_populates="posts")

# Define the Comment model
class Comment(Base):
    __tablename__ = "comments"

    # Define columns
    id = Column(Integer(), primary_key=True)
    comment_text = Column(Text(), nullable=False)

    # Define foreign keys
    post_id = Column(Integer(), ForeignKey('blog_posts.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))

    # Define many-to-one relationship with blog posts and users
    blog_post = relationship("BlogPost", back_populates="comments")
    user = relationship("User", back_populates="comments")
