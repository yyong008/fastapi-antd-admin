from __future__ import annotations  # This allows the use of forward references
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# from app.schemas.sys.role import Role


class MenuBase(BaseModel):
    name: str = Field(..., title="Menu Name", description="The name of the menu")
    type: int = Field(..., title="Menu Type", description="The type of the menu")
    description: Optional[str] = Field(
        None, title="Description", description="A brief description of the menu"
    )
    remark: Optional[str] = Field(
        None, title="Remark", description="Any additional remarks"
    )
    icon: Optional[str] = Field(None, title="Icon", description="Icon for the menu")
    path: Optional[str] = Field(None, title="Path", description="The path of the menu")
    path_file: Optional[str] = Field(
        None, title="File Path", description="The file path associated with the menu"
    )
    status: Optional[int] = Field(
        None, title="Status", description="The status of the menu"
    )
    isShow: Optional[int] = Field(
        None, title="Is Show", description="Flag indicating if the menu is visible"
    )
    isCache: Optional[int] = Field(
        None, title="Is Cache", description="Flag indicating if the menu is cached"
    )
    permission: Optional[str] = Field(
        None, title="Permission", description="Permission identifier for the menu"
    )
    isLink: Optional[int] = Field(
        None,
        title="Is Link",
        description="Flag indicating if the menu is an external link",
    )
    order_no: Optional[int] = Field(
        None, title="Order No", description="The order number of the menu"
    )


class MenuCreate(MenuBase):
    parent_menu_id: Optional[int] = Field(
        None, title="Parent Menu ID", description="ID of the parent menu"
    )


class MenuUpdate(MenuBase):
    parent_menu_id: Optional[int] = Field(
        None, title="Parent Menu ID", description="ID of the parent menu"
    )

class MenuDeleteByIds(BaseModel):
    ids: List[int] = Field(..., title="Menu IDs", description="List of menu IDs to delete")
# class MenuInDBBase(MenuBase):
#     id: int
#     created_at: datetime
#     updated_at: Optional[datetime]

#     class Config:
#         from_attributes = True


# class Menu(MenuInDBBase):
#     parent_menu: Optional[Menu] = None  # Use string annotation for forward reference
#     children_menu: List[Menu] = []  # Use string annotation for forward reference
#     roles: List[Role] = []  # Use string annotation for forward reference


# class MenuInDB(MenuInDBBase):
#     pass
