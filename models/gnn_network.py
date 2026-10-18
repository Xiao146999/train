"""GNN 座位分配网络（骨架占位，等待填充）。

设计意图：
  1. 以 PyG 的 HeteroData 表示「订单节点 / 乘客节点 / 座位节点」的异构图；
  2. 用 SCIP 夜间批处理的最优解作为伪标签，做有监督 / 自训练；
  3. 推理时输出每条 (订单, 座位) 边的匹配概率，供实时引擎兜底排序。
"""

from __future__ import annotations


class SeatGNN:
    """基于异构图的座位分配网络（占位骨架）。"""

    def __init__(self, hidden_dim: int = 64, num_layers: int = 2) -> None:
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        # TODO: 构建 HeteroConv / SAGEConv 等消息传递层
        # TODO: 定义 order -> seat 的打分头 (edge decoder)

    def forward(self, hetero_data):
        """输入 PyG HeteroData，输出每个 (订单, 座位) 边的匹配概率。"""
        raise NotImplementedError("等待填充骨架代码")

    def save(self, path: str) -> None:
        """保存训练后的权重。"""
        raise NotImplementedError("等待填充骨架代码")

    def load(self, path: str) -> None:
        """加载训练后的权重。"""
        raise NotImplementedError("等待填充骨架代码")
