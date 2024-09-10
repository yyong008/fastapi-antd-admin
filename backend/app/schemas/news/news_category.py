from pydantic import BaseModel, Field
from typing import Optional, List

from app.schemas.news.news import News


class NewsCategoryBase(BaseModel):
    name: str = Field(
        ..., title="Name", description="The unique name of the news category"
    )
    description: Optional[str] = Field(
        None, title="Description", description="A brief description of the category"
    )
    user_id: int = Field(
        ...,
        title="User ID",
        description="The ID of the user associated with the category",
    )


class NewsCategoryCreate(NewsCategoryBase):
    pass


class NewsCategoryUpdate(NewsCategoryBase):
    pass


class NewsCategoryInDBBase(NewsCategoryBase):
    id: int

    class Config:
        orm_mode = True


class NewsCategory(NewsCategoryInDBBase):
    news: List["News"] = []  # Forward reference to News


class NewsCategoryInDB(NewsCategoryInDBBase):
    pass
