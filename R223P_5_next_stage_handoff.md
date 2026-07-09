# R223P-5 next stage handoff

stage_id: 1013R_R223P_5_V0_2_LOCK_CANDIDATE  
status: handoff

## 当前状态

```text
R223P-5 = PASS_LOCK_R223M_STANDARD_V0_2_CANDIDATE
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI = BLOCKED
```

## 后续允许方向

下一步不能直接 UI，也不能 formal apply。建议下一步只做以下之一：

```text
R223Q_TRUE_GENERATION_REGRESSION_GATE
或
R223P-6_V0_2_CANDIDATE_REAL_GENERATION_FIXTURE
```

目标应是用 v0.2 candidate 做真实生成 fixture 回归，验证：

1. 生成器能否正确填 review ledger。
2. 教师默认稿是否继续自然。
3. 新字段是否不会造成模板腔或字段墙。
4. unit intensity router 是否能影响展开密度。
5. 未注册组件是否仍不进入教师默认稿。

## 仍然禁止

```text
不改 R97B
不改 frontend/backend
不接 runtime
不接 provider/model
不改 prompt
不建数据库
不改 R223M/N/O 既有稿
不改 R222D 组件库
不发布正式 v0.2
不 formal apply
```

## 给下游的关键提醒

v0.2 candidate 的价值在于“更好地控制课堂展开密度和美术实践模式”，不是让字段更多。任何下游实现都必须先保护教师默认阅读层。

