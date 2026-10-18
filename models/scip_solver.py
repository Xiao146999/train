from pyscipopt import Model
from src.schemas.order import Order

class SCIPSolver:
    def solve(self, orders: list[Order]):
        model = Model("RailwaySeatMILP")
        
        # TODO: 把订单和座位转化为 0-1 变量
        # x[i, s] 代表订单 i 分配到座位 s
        
        # TODO: 添加约束 P0 (每人一座、库存限制)
        # TODO: 添加约束 P1/P2 (重点旅客、家庭强绑定)
        
        # model.optimize()
        print("SCIP 运筹求解中...")
        return [] # 返回分配矩阵
