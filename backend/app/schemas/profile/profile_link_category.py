from typing import Optional
from pydantic import BaseModel, Field


class LinkCategoryCreate(BaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name or title of the link category",
    )
    description: Optional[str] = Field(
        None,
        title="Description",
        description="A brief description of the link category",
    )
    user_id: int = Field(
        None,
        title="User ID",
        description="The ID of the user associated with the link category",
    )

class LinkCategoryUpdate(BaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name or title of the link category",
    )
    description: Optional[str] = Field(
        None,
        title="Description",
        description="A brief description of the link category",
    )
    user_id: int = Field(
        None,
        title="User ID",
        description="The ID of the user associated with the link category",
    )

class LinkCategoryDeleteByIds(BaseModel):
    ids: list[int]
