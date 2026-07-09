# R223P-5 unit lesson practice intensity router contract

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
status: router_contract_candidate

## 合同目标

大单元中的每一课不应采用同一课堂展开密度。router 先判断课时责任，再决定系统生成多少讲解、示范、小练、创作支架、巡视观察点和评价证据。

## 候选字段

```json
{
  "unit_phase_role": "intro_understanding | technique_preparation | practice_creation | showcase_evaluation | transfer_closure | project_synthesis",
  "lesson_position_in_unit": "early | middle | late | final | standalone_unknown",
  "practice_intensity": "low | medium | high",
  "student_work_time_ratio": "low | medium | high",
  "teacher_support_density": "light | normal | heavy",
  "performance_task_link": "...",
  "stage_evidence_link": "..."
}
```

## 路由规则

| unit_phase_role | 生成重心 | 避免 |
| --- | --- | --- |
| intro_understanding | 观察、问题建立、赏析、轻实验 | 大量创作辅导 |
| technique_preparation | 示范、小练、材料实验、错误修补 | 复杂单元表现任务 |
| practice_creation | 创作推进、巡视观察、过程证据、补救策略 | 长篇概念讲解 |
| showcase_evaluation | 作品说明、自评互评、证据归档、二改建议 | 新技法讲授 |
| transfer_closure | 方法收束、迁移任务、单元成果连接 | 重创作流程 |
| project_synthesis | 项目进度、分工、综合证据链 | 单点技能练习 |

## P4 回归结果

| sample | unit_phase_role | practice_intensity | 证明 |
| --- | --- | --- | --- |
| 我为文具代言 | practice_creation | high | 重创作、重巡视、重过程证据 |
| 有趣的纸印 | technique_preparation | medium | 材料观察、示范、小练、作品保底 |
| 色彩的碰撞 | intro_understanding | medium | 色彩问题建立、调色实验、表达收束 |

## 教师默认稿

router 字段不直接显示。教师只看到自然化内容，例如“本课位于……阶段”“本节课先观察，再做小样试验”。

## 边界

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
router 当前是 candidate contract，不接 runtime，不写库，不改既有教师稿。
```
