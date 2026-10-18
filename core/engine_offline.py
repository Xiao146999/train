from src.schemas.order import Order
from src.models.scip_solver import SCIPSolver

class OfflineEngine:
    def __init__(self):
        self.scip_solver = SCIPSolver()

    def run_nightly_batch(self, orders: list[Order]):
        """
        夜间批处理: T-16晚23:00 运行
        """
        print(f"开始处理 {len(orders)} 个预约订单...")
        # 1. 调用 SCIP 求解全局最优
        optimal_matrix = self.scip_solver.solve(orders)
        
        # 2. 用最优矩阵生成 GNN 的伪标签 (PyG格式)
        # TODO: 构建异构图数据
        
        # 3. 触发 GNN 训练流水线
        print("SCIP 打标完成，GNN 训练任务已提交。")
        return optimal_matrix
