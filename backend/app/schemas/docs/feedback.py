from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class FeedBackBase(BaseModel):
    user_id: int = Field(
        ...,
        title="User ID",
        description="The ID of the user who submitted the feedback",
    )
    content: str = Field(
        ..., title="Content", description="The feedback content provided by the user"
    )
    url: Optional[str] = Field(
        None, title="URL", description="The URL of the feedback image"
    )
    created_at: Optional[datetime] = Field(
        None, title="Created At", description="The time when the feedback was created"
    )
    updated_at: Optional[datetime] = Field(
        None,
        title="Updated At",
        description="The time when the feedback was last updated",
    )


class FeedBackCreate(FeedBackBase):
    pass


class FeedBackUpdate(FeedBackBase):
    pass


class FeedBackInDBBase(FeedBackBase):
    id: int

    class Config:
        orm_mode = True


class FeedBack(FeedBackInDBBase):
    pass


class FeedBackInDB(FeedBackInDBBase):
    pass
