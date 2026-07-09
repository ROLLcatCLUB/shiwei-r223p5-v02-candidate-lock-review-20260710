# R223P-5 regression summary from P4

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
source_stage: R223P-4_THREE_SAMPLE_REGRESSION

## P4 结论

```text
R223P-4 = PASS_THREE_SAMPLE_REGRESSION
decision = PASS_CONTINUE_TO_R223P_5_V0_2_LOCK_CANDIDATE
```

## 三样本结果

| sample | 课型侧重 | unit_phase_role | practice_intensity | result |
| --- | --- | --- | --- | --- |
| 我为文具代言 | 设计应用 / 生活问题解决 | practice_creation | high | PASS |
| 有趣的纸印 | 材料技法 / 印痕探究 | technique_preparation | medium | PASS |
| 色彩的碰撞 | 视觉语言 / 色彩感知 | intro_understanding | medium | PASS |

## 回归确认

- 三样本均可标注 primary `practice_pattern_type`。
- 三样本均可区分 `unit_phase_role + practice_intensity`。
- 条件字段只在对应事件启用。
- 组件触发均带状态。
- 教师默认稿未出现禁止字段名。
- 三样本无内容互相污染。
- 字段 delta 没有导致教师稿变重。

## P5 采用结论

P5 可以锁定 v0.2 candidate，但仍不得发布正式 v0.2。

