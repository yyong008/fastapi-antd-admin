from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ChangeLogBase(BaseModel):
    user_id: int = Field(
        ..., title="User ID", description="The ID of the user who made the change"
    )
    publish_name: str = Field(
        ..., title="Publish Name", description="The name of the publisher"
    )
    publish_version: str = Field(
        ..., title="Publish Version", description="The version of the published update"
    )
    publish_time: datetime = Field(
        ..., title="Publish Time", description="The time when the change was published"
    )
    type: int = Field(
        ...,
        title="Type",
        description="The type of change: 1 for major update, 2 for feature update, 3 for bug fix",
    )
    content: str = Field(..., title="Content", description="Details about the change")
    url: str = Field(
        ..., title="URL", description="The URL for more information about the update"
    )
    created_at: Optional[datetime] = Field(
        None, title="Created At", description="The time when this record was created"
    )
    updated_at: Optional[datetime] = Field(
        None,
        title="Updated At",
        description="The time when this record was last updated",
    )


class ChangeLogCreate(ChangeLogBase):
    pass


class ChangeLogUpdate(ChangeLogBase):
    pass


class ChangeLogInDBBase(ChangeLogBase):
    id: int

    class Config:
        orm_mode = True


class ChangeLog(ChangeLogInDBBase):
    pass


class ChangeLogInDB(ChangeLogInDBBase):
    pass
