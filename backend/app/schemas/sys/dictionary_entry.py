from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class DictionaryEntryBase(BaseModel):
    key: str = Field(
        ..., title="Entry Key", description="The key of the dictionary entry"
    )
    value: str = Field(
        ..., title="Entry Value", description="The value of the dictionary entry"
    )
    order_no: Optional[int] = Field(
        None, title="Order No", description="The order number of the entry"
    )
    status: int = Field(
        ..., title="Status", description="The status of the dictionary entry"
    )
    remark: Optional[str] = Field(
        None, title="Remark", description="Any additional remarks"
    )


class DictionaryEntryCreate(DictionaryEntryBase):
    pass


class DictionaryEntryUpdate(DictionaryEntryBase):
    pass


class DictionaryEntryInDBBase(DictionaryEntryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class DictionaryEntry(DictionaryEntryInDBBase):
    dictionary_id: int


class DictionaryEntryInDB(DictionaryEntryInDBBase):
    pass
