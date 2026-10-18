from pydantic import BaseModel
from enum import Enum
from typing import List, Optional

class PassengerType(str, Enum):
    ADULT = "adult"
    CHILD = "child"
    INFANT = "infant"      # 婴儿 (不能进静音车厢)
    WHEELCHAIR = "wheelchair" # 轮椅 (必须在7车)

class Passenger(BaseModel):
    passenger_id: str
    p_type: PassengerType
    has_infant: bool = False

class Order(BaseModel):
    """订单模型"""
    order_id: str
    passengers: List[Passenger]
    prefer_window: bool = False
    assigned_seats: List[str] = [] # 分配到的座位ID列表
