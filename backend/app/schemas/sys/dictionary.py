from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

from app.schemas.sys.dictionary_entry import DictionaryEntry


class DictionaryBase(BaseModel):
    name: str = Field(
        ..., title="Dictionary Name", description="The name of the dictionary"
    )
    code: str = Field(
        ..., title="Code", description="The unique code for the dictionary"
    )
    description: Optional[str] = Field(
        None, title="Description", description="A brief description of the dictionary"
    )
    remark: Optional[str] = Field(
        None, title="Remark", description="Any additional remarks"
    )
    status: Optional[int] = Field(
        None, title="Status", description="The status of the dictionary"
    )


class DictionaryCreate(DictionaryBase):
    pass


class DictionaryUpdate(DictionaryBase):
    pass


class DictionaryInDBBase(DictionaryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class Dictionary(DictionaryInDBBase):
    entries: List[DictionaryEntry] = []


class DictionaryInDB(DictionaryInDBBase):
    pass
