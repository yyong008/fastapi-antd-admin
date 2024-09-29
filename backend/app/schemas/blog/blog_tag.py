from pydantic import BaseModel, Field
from typing import Optional


class BlogTagBase(BaseModel):
    name: str = Field(..., title="Name", description="The name of the blog tag")
    description: Optional[str] = Field(
        None, title="Description", description="A description of the blog tag"
    )
    user_id: Optional[int] = Field(
        None, title="User ID", description="The ID of the user who created the blog tag"
    )


class BlogTagCreate(BlogTagBase):
    pass


class BlogTagUpdate(BlogTagBase):
    pass


class BlogTagInDBBase(BlogTagBase):
    id: int

    class Config:
        from_attributes = True

class BlogTagDeleteByIds(BaseModel):
    ids: list[int]
