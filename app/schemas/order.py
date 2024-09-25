from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional


class OrderItemBase(BaseModel):
    product_id: int
    stock: int = Field(..., gt=0)


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int
    order_id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    status: Optional[str] = "в процессе"


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderStatusUpdate(BaseModel):
    status: str


class Order(OrderBase):
    id: int
    created_at: datetime
    items: List[OrderItem]

    class Config:
        orm_mode = True


class OrderList(BaseModel):
    orders: List[Order]

    class Config:
        orm_mode = True
