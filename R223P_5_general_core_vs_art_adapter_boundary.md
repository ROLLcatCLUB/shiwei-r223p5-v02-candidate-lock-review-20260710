# R223P-5 general core vs art adapter boundary

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
status: boundary_lock_candidate

## general_pedagogy_core

通用教学推理底座描述课时角色、实践密度、证据、检查点和分支条件。未来科学、语文、数学等学科可复用这一层。

```text
unit_phase_role
lesson_position_in_unit
practice_intensity
student_work_time_ratio
teacher_support_density
performance_task_link
stage_evidence_link
process_evidence
checkpoint
branch_to
exit_condition
```

## art_subject_adapter

美术学科实践模式适配层描述美术课堂独有的观察、比较、赏析、示范、小练、材料实验、创作推进、展示评价和审美语言。

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

## 不可混淆

- `practice_pattern_type` 不等于通用教学法字段。
- `aesthetic_language_focus` 不应迁移到数学/语文/科学通用 schema。
- 科学、语文、数学后续应替换学科实践模式库，而不是重写通用底座。
- 美术 adapter 可以为其他学科提供分层范式，但不能直接泛化。

## 后续迁移原则

```text
保留：unit_phase_role / practice_intensity / checkpoint / process_evidence
替换：art_subject_adapter practice pattern registry
重做：学科特有证据、材料、语言、任务类型
```

## 边界

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
本文件只锁定通用底座与美术适配层边界，不发布正式 v0.2。
```
