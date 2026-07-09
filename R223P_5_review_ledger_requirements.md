# R223P-5 review ledger requirements

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
status: review_ledger_requirements_lock

## review ledger 责任

review ledger 保存教师默认稿不应直接显示、但系统生成和审核必须追踪的信息。

## 必须保存

```text
event_id
source_anchor
unit_phase_role
practice_intensity
primary_pattern
secondary_patterns
activated_adapter_fields
screen_trigger
component_trigger
component_trigger_status
learning_sheet_fields
evidence_outputs
assessment_alignment
checkpoint
process_evidence
source_status
validator_rule_id
```

## 组件状态要求

每个 `component_trigger` 必须有状态：

```text
already_registered
candidate_from_R222D_pool
new_surface_candidate
unregistered_do_not_execute
```

## ledger 与教师稿关系

```text
review ledger = 可追溯、可验证、可回归
teacher default = 可阅读、可修改、可上课
```

ledger 不能直接铺到教师默认稿里，教师稿也不能删除 ledger 中必要的生成依据。

## P5 注意

P5 不要求回写 R223M/N/O 既有 ledger。后续真实生成回归时，应按本文件生成统一 JSON ledger。

## 边界

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
本文件只锁定 review ledger candidate requirements，不改现有 ledger，不 formal apply。
```
