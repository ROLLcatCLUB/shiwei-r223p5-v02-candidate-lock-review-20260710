# R223P-5 field required / optional / ledger-only policy

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
status: policy_lock_candidate

## required candidate

这些字段在 v0.2 candidate 中作为候选必备，但正式 required 仍需后续真实生成回归确认。

| field_id | 层级 | required 条件 |
| --- | --- | --- |
| unit_phase_role | general_pedagogy_core | lesson-level required candidate |
| practice_intensity | general_pedagogy_core | lesson-level required candidate |
| practice_pattern_type | art_subject_adapter | review ledger primary pattern required candidate |

## conditional required

| field_id | 条件 |
| --- | --- |
| process_evidence | practice_creation 或 micro_practice 存在 |
| checkpoint | practice_creation 高实践密度课时 |
| student_practice_output | micro_practice_type 存在 |
| transition_to_formal_creation | micro_practice_type 存在，或 demonstration_type 后接正式创作 |
| material_safety_or_management | material_experiment 涉及材料、工具、清理或安全风险 |
| evidence_outputs | showcase_evaluation 事件 |

## optional

| field_id | 说明 |
| --- | --- |
| lesson_position_in_unit | 建议填写，但可为 standalone_unknown |
| student_work_time_ratio | 用于密度估计，不强制 |
| teacher_support_density | 用于支架密度估计，不强制 |
| performance_task_link | 单元表现性任务存在时建议 |
| stage_evidence_link | 建议 |
| branch_to | 分支决策时使用 |
| exit_condition | 建议 |
| artwork_reference_type | 有作品资源时使用 |
| aesthetic_language_focus | 视觉语言类、赏析类、色彩类建议 |
| technique_breakthrough_point | 技法突破时建议 |

## review ledger only

```text
component_trigger_status
screen_trigger.details
learning_sheet_fields
evidence_trigger.details
unregistered_surface_candidates
validator_rule_id
source_status
activated_adapter_fields
primary_pattern
secondary_patterns
```

## 教师默认稿原则

教师默认稿只看自然化后的课堂语言，不显示字段名，不显示组件状态，不显示 validator 规则。

## 边界

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
本文件只锁定候选字段策略，不发布正式 schema，不触发 formal apply。
```
