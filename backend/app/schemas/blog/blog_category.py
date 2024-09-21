from pydantic import BaseModel, Field
from typing import Optional


class BlogCategoryBase(BaseModel):
    name: str = Field(..., title="Name", description="The name of the blog category")
    description: Optional[str] = Field(
        None, title="Description", description="A description of the blog category"
    )
    user_id: int = Field(
        ...,
        title="User ID",
        description="The ID of the user who created the blog category",
    )


class BlogCategoryCreate(BlogCategoryBase):
    pass


class BlogCategoryUpdate(BlogCategoryBase):
    pass


class BlogCategoryInDBBase(BlogCategoryBase):
    id: int

    class Config:
        from_attributes = True


class BlogCategory(BlogCategoryInDBBase):
    pass


class BlogCategoryInDB(BlogCategoryInDBBase):
    pass
