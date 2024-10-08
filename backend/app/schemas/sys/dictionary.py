from pydantic import BaseModel, Field
from typing import Optional


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


class DictionaryDeleteByIds(BaseModel):
    ids: list[int]
