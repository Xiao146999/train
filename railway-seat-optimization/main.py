import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.core.engine_online import RealtimeEngine
from src.schemas.order import Order, Passenger, PassengerType
from src.schemas.seat import Seat

if __name__ == "__main__":
    print("🚄 高铁选座双引擎系统启动...")
    
    # 造几个假数据测试一下
    test_seat = Seat(seat_id="02A", car_number=2, row=1, col="A")
    engine = RealtimeEngine(available_seats=[test_seat])
    
    # 模拟一个带娃家庭
    order = Order(
        order_id="ORD_001",
        passengers=[
            Passenger(passenger_id="P1", p_type=PassengerType.ADULT),
            Passenger(passenger_id="P2", p_type=PassengerType.CHILD)
        ]
    )
    
    success = engine.allocate(order)
    print(f"出票状态: {'成功' if success else '失败'}")
