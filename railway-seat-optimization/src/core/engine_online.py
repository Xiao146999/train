from src.schemas.order import Order
from src.schemas.seat import Seat
from src.utils.alert_system import generate_alert_ticket

class RealtimeEngine:
    def __init__(self, available_seats: list[Seat]):
        self.available_seats = available_seats

    def allocate(self, order: Order) -> bool:
        """
        实时单分配核心逻辑 (毫秒级)
        返回: 是否成功出票
        """
        # 1. 硬约束尝试 (P0-P1): 过滤婴儿/轮椅座位
        candidates = self._filter_hard_constraints(order)
        
        # 2. 降级机制: 如果没有满足硬约束的座位，强制降级
        if not candidates:
            candidates = self.available_seats
            # TODO: 记录降级事件，准备生成工单
            is_degraded = True
        else:
            is_degraded = False
            
        # 3. 分配座位 (P2-P3: 优先连座同车厢)
        if candidates:
            # TODO: 实现连座贪心算法，扣减库存
            # self._deduct_inventory(order, assigned_seats)
            
            # 4. 如果触发了降级，生成警报
            if is_degraded:
                generate_alert_ticket(order, reason="余票不足，强制降级分配")
                
            return True # 绝不卡单，成功出票
        
        return False

    def _filter_hard_constraints(self, order: Order) -> list[Seat]:
        """根据乘客属性过滤座位"""
        # TODO: 实现过滤逻辑 (例如婴儿过滤2车)
        return self.available_seats
