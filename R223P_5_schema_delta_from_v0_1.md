# R223P-5 schema delta from v0.1

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
status: candidate_delta_lock

## v0.1 保留

v0.2 candidate 继承 R223M-P5 v0.1 的课堂事件基本结构：

```text
event_id
event_name
section
source_anchor
teaching_responsibility
student_problem
task_release
expected_student_responses
likely_misconceptions_or_failures
teacher_follow_up_questions
teacher_scaffolding_moves
teacher_rescue_strategy
screen_trigger
component_trigger
learning_sheet_trigger
evidence_trigger
assessment_alignment
transition_chain
teacher_visible_note
control_points
```

## v0.2 candidate 新增方向

### 1. 大单元课时路由

```text
unit_phase_role
lesson_position_in_unit
practice_intensity
student_work_time_ratio
teacher_support_density
performance_task_link
stage_evidence_link
```

解决问题：不同课时承担不同大单元责任，不能统一展开为同一种练习密度。

### 2. 通用过程控制

```text
process_evidence
checkpoint
branch_to
exit_condition
```

解决问题：课堂展开需要明确何时观察、何时补救、何时进入下一环节。

### 3. 美术学科实践模式

```text
practice_pattern_type
demonstration_type
micro_practice_type
appreciation_scaffold_type
artwork_reference_type
aesthetic_language_focus
technique_breakthrough_point
material_safety_or_management
student_practice_output
transition_to_formal_creation
```

解决问题：美术课有观察、赏析、示范、小练、材料实验、创作推进、展示评价等学科实践模式，不能只靠通用环节标题表达。

### 4. review ledger only 控制

```text
component_trigger_status
unregistered_surface_candidates
validator_rule_id
activated_adapter_fields
primary_pattern
secondary_patterns
```

解决问题：结构化审核需要完整记录，但教师默认稿不能被字段污染。

## 不变边界

P5 不覆盖 v0.1 历史包，不改变 R223M/N/O 教师稿，不发布正式 v0.2。

