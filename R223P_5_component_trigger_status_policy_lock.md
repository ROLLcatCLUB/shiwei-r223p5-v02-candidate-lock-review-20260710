# R223P-5 component trigger status policy lock

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
status: component_status_policy_locked_candidate

## 状态枚举

| status | 含义 | 默认行为 |
| --- | --- | --- |
| already_registered | 已在 R222D/R222D-P1 组件库中出现并有教学责任定义 | 可进入 review ledger，仍不可执行 |
| candidate_from_R222D_pool | 与已有码表或组件候选相近，需要命名治理 | 只能进入 review ledger |
| new_surface_candidate | 新课堂 surface 候选，需要后续组件库治理 | 只能进入 review ledger |
| unregistered_do_not_execute | 未注册且不得执行 | 禁止进入教师默认稿和 UI |

## 硬规则

1. P5 不改 R222D 组件库。
2. 组件状态不等于 runtime 可执行权限。
3. 新 surface 候选不得进入教师默认稿。
4. 未注册组件不得进入教师默认稿。
5. 所有组件触发必须服务明确课堂事件和学生问题。

## P4 回归证明

三样本中出现的组件候选均可标注状态；新 surface 候选没有进入教师默认稿。

