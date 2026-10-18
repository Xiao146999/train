from pydantic import BaseModel
from typing import List

class Seat(BaseModel):
    """物理座位模型"""
    seat_id: str
    car_number: int      # 车厢号 (1-8)
    row: int             # 排号
    col: str             # 列号 (A, B, C, D, F)
    is_window: bool = False
    is_aisle: bool = False
