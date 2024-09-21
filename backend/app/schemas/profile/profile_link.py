from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

from app.schemas.profile.profile_link_category import LinkCategory


class LinkBase(BaseModel):
    name: str = Field(..., title="Name", description="The name or title of the link")
    url: HttpUrl = Field(
        ..., title="URL", description="The actual URL that the link points to"
    )
    description: Optional[str] = Field(
        None, title="Description", description="A brief description of the link"
    )
    user_id: int = Field(
        ..., title="User ID", description="The ID of the user associated with the link"
    )
    category_id: int = Field(
        ...,
        title="Category ID",
        description="The ID of the category this link belongs to",
    )


class LinkCreate(LinkBase):
    pass


class LinkUpdate(LinkBase):
    pass


class LinkInDBBase(LinkBase):
    id: int

    class Config:
        from_attributes = True


class Link(LinkInDBBase):
    category: Optional[LinkCategory] = None  # Forward reference to LinkCategory


class LinkInDB(LinkInDBBase):
    pass
