# Import the BaseModel class from Pydantic
from pydantic import BaseModel

# Define Pydantic schema for creating a new blog post
class BlogPostCreate(BaseModel):
    title: str
    category: str
    subCategory: str
    content: str
    authorName: str
    authorAvatar: str
    cover: str

# Define Pydantic schema for the response when creating or retrieving a blog post
class BlogPostResponse(BlogPostCreate):
    id: int
    createdAt: str

# Define Pydantic schema for user input data
class UserSchema(BaseModel):
    name: str
    phone: str

# Define Pydantic schema for comment input data
class CommentSchema(BaseModel):
    comment_text: str

# Define Pydantic schema for the response when creating or retrieving a comment
class CommentResponse(CommentSchema):
    id: int

# Define Pydantic schema for the response when creating or retrieving a user
class UserResponse(UserSchema):
    id: int
