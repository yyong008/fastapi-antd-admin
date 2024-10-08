from pydantic import BaseModel, Field
from typing import Optional


class NewsCategoryBase(BaseModel):
    name: str = Field(
        ..., title="Name", description="The unique name of the news category"
    )
    description: Optional[str] = Field(
        None, title="Description", description="A brief description of the category"
    )
    user_id: Optional[str] = Field(
        None,
        title="User ID",
        description="The ID of the user associated with the category",
    )


class NewsCategoryCreate(NewsCategoryBase):
    pass

class NewsCategoryDeleteByIds(BaseModel):
    ids: list[int]

class NewsCategoryUpdate(NewsCategoryBase):
    pass


class NewsCategoryInDBBase(NewsCategoryBase):
    id: int

    class Config:
        from_attributes = True
