# R223P-5 teacher default view guardrails

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
status: teacher_default_guardrails_lock

## 教师默认稿定位

教师默认稿必须是成熟教案文稿，不是字段墙、模式表、组件货架或 review ledger。

## 禁止直接显示字段名

```text
practice_pattern_type
demonstration_type
micro_practice_type
appreciation_scaffold_type
component_trigger
component_trigger_status
screen_trigger
learning_sheet_fields
validator_rule_id
activated_adapter_fields
primary_pattern
secondary_patterns
```

## 允许自然化呈现

| 结构字段 | 自然化写法 |
| --- | --- |
| unit_phase_role | 本课处在单元的…… |
| practice_intensity | 本课以观察 / 小练 / 创作为主 |
| checkpoint | 巡视时重点看…… |
| process_evidence | 至少留下…… |
| aesthetic_language_focus | 引导学生关注冷暖、明暗、肌理、边缘等 |
| transition_to_formal_creation | 完成小练后，把方法用到正式作品中 |

## 默认稿质量线

1. 先看课时定位、目标、准备、结构、过程、评价。
2. 教学过程保持阶段、活动、教师话术、学生反应、追问、设计意图。
3. 下游大屏、学习单、评价证据只做自然落点，不压正文。
4. 未注册组件和新 surface 候选不得出现在默认稿中。
5. 不因 validator 字段变多而让教师稿变重。

## P4 回归结果

三样本教师默认稿均未出现禁止字段名，且未回到卡片墙或组件货架。

