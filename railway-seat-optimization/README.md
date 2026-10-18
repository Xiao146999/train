# 高铁选座双引擎系统（railway-seat-optimization）

面向 CRH2C 车型的「实时 + 离线」双引擎选座项目：**实时引擎绝不卡单**，在毫秒级完成出票（必要时降级并生成工单）；**离线引擎**每天夜间用 SCIP 求全局最优，产出伪标签驱动 GNN 学习，逐步替代求解器。

> 当前状态：**骨架阶段**。目录、配置、数据模型和引擎接口已就位，核心算法（过滤、连座贪心、MILP 建模、GNN 构图）以待填充的 `TODO` 标记。

## 目录结构

```text
railway-seat-optimization/
├── configs/
│   └── business_rules.yaml      # 车型拓扑 + 约束优先级定义
├── src/
│   ├── __init__.py
│   ├── schemas/                 # 数据模型层（物理底座）
│   │   ├── order.py             #   Order / Passenger / PassengerType
│   │   └── seat.py              #   Seat（车厢、排、列、靠窗/过道）
│   ├── core/
│   │   ├── engine_online.py     # 实时引擎：P0-P3 分配 + 降级兜底
│   │   └── engine_offline.py    # 离线引擎：夜间批处理调度
│   ├── models/
│   │   ├── scip_solver.py       # SCIP MILP 全局最优
│   │   └── gnn_network.py       # GNN 异构图表征（占位）
│   └── utils/
│       └── alert_system.py      # 降级警报 / 乘务员工单
├── tests/
│   └── __init__.py
├── main.py                      # 冒烟入口
├── requirements.txt
├── .gitignore
└── README.md
```

## 引擎分工

| 引擎 | 触发时机 | 目标 | 关键约束 |
| --- | --- | --- | --- |
| 实时引擎 `RealtimeEngine` | 用户下单瞬间 | 毫秒级、**绝不卡单** | P0 库存/区间冲突、P1 重点旅客；不满足则降级出票 + 工单 |
| 离线引擎 `OfflineEngine` | T-16 晚 23:00 批处理 | 全局座位利用率最优 | P0-P5 全量建模，SCIP 求 MILP |

`configs/business_rules.yaml` 中的 P0-P5 即约束优先级：P0 库存不超卖、P1 重点旅客合规（轮椅必在 7 车、婴儿避开 2 车）、P2 成人与儿童强绑定同车厢、P3 成人与成人弱绑定、P4 靠窗/过道偏好、P5 全局利用率最大化。

## 环境准备

```bash
# 建议先建虚拟环境（Python 3.10+）
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

> `pyscipopt` 与 `torch-geometric` 体积较大，首次安装耗时较长；若只验证实时引擎骨架，装 `pydantic` 即可。

## 运行

```bash
python main.py
```

预期输出：

```text
🚄 高铁选座双引擎系统启动...
出票状态: 成功
```

（当前 `allocate()` 恒返回 `True`，`_filter_hard_constraints()` 原样返回全部座位——这是骨架的「绝不卡单」保底行为。）

## 待填充清单

- [ ] `src/core/engine_online.py`：`_filter_hard_constraints` 硬约束过滤、连座贪心 + 库存扣减（P2-P3）
- [ ] `src/models/scip_solver.py`：0-1 决策变量、P0-P5 约束、目标函数
- [ ] `src/core/engine_offline.py`：由最优矩阵构建 PyG 异构图、触发 GNN 训练
- [ ] `src/models/gnn_network.py`：异构图消息传递层与边打分头
- [ ] `src/utils/alert_system.py`：工单落库 / 前端红字弹窗推送
- [ ] `tests/`：硬约束、降级路径、库存一致性的单元测试
