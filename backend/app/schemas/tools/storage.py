from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class StorageBase(BaseModel):
    user_id: int = Field(
        ..., title="User ID", description="ID of the user who uploaded the file"
    )
    name: str = Field(..., title="Name", description="Name of the file")
    file_name: str = Field(
        ..., title="File Name", description="Actual file name as stored"
    )
    ext_name: str = Field(..., title="Extension", description="File extension")
    path: str = Field(..., title="Path", description="Path to the file")
    size: str = Field(..., title="Size", description="Size of the file")
    type: str = Field(..., title="Type", description="Type of the file")


class StorageCreate(StorageBase):
    pass


class StorageUpdate(StorageBase):
    pass


class StorageInDBBase(StorageBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = Field(
        None, title="Updated At", description="Last time the record was updated"
    )

    class Config:
        from_attributes = True


class Storage(StorageInDBBase):
    pass


class StorageInDB(StorageInDBBase):
    pass
