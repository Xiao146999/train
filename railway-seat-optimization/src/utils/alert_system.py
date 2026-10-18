from src.schemas.order import Order

def generate_alert_ticket(order: Order, reason: str):
    """
    生成乘务员工单并触发支付页红字弹窗
    """
    print(f"🚨 [警报工单] 订单 {order.order_id} 触发降级！原因: {reason}")
    # TODO: 推送消息到前端(红字弹窗) 或 保存到数据库供乘务员端拉取
