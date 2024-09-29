from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class BlogBase(BaseModel):
    title: str = Field(..., title="Title", description="The title of the blog post")
    content: str = Field(
        ..., title="Content", description="The content of the blog post"
    )
    author: Optional[str] = Field(
        None, title="Author", description="The author of the blog post"
    )
    source: Optional[str] = Field(
        None, title="Source", description="The source of the blog post"
    )
    viewCount: int = Field(
        0, title="View Count", description="The number of views for the blog post"
    )
    publishedAt: datetime = Field(
        None, title="Published At", description="The publication date of the blog post"
    )
    user_id: int = Field(
        None, title="User ID", description="The ID of the user who created the blog post"
    )
    category_id: int = Field(
        ..., title="Category IDs", description="List of category IDs"
    )
    tag_id: int = Field(..., title="Tag IDs", description="List of tag IDs")


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogInDBBase(BlogBase):
    id: int

    class Config:
        from_attributes = True

class BlogDeleteByIds(BaseModel):
    ids: list[int]
