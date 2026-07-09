import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223P_5_v0_2_candidate_lock_report.md",
    "R223P_5_classroom_event_schema_v0_2_candidate.json",
    "R223P_5_schema_delta_from_v0_1.md",
    "R223P_5_field_required_optional_ledger_only_policy.md",
    "R223P_5_general_core_vs_art_adapter_boundary.md",
    "R223P_5_unit_lesson_practice_intensity_router_contract.md",
    "R223P_5_teacher_default_view_guardrails.md",
    "R223P_5_review_ledger_requirements.md",
    "R223P_5_component_trigger_status_policy_lock.md",
    "R223P_5_regression_summary_from_P4.md",
    "R223P_5_next_stage_handoff.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]

GENERAL_FIELDS = [
    "unit_phase_role",
    "lesson_position_in_unit",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
    "process_evidence",
    "checkpoint",
    "branch_to",
    "exit_condition",
]

ART_FIELDS = [
    "practice_pattern_type",
    "demonstration_type",
    "micro_practice_type",
    "appreciation_scaffold_type",
    "artwork_reference_type",
    "aesthetic_language_focus",
    "technique_breakthrough_point",
    "material_safety_or_management",
    "student_practice_output",
    "transition_to_formal_creation",
]

LEDGER_FIELDS = [
    "component_trigger_status",
    "screen_trigger.details",
    "learning_sheet_fields",
    "evidence_trigger.details",
    "unregistered_surface_candidates",
]

FORBIDDEN_TRUE_FLAGS = [
    "schema_v0_2_published",
    "r223m_p5_v0_1_modified",
    "existing_teacher_drafts_modified",
    "r222d_component_library_modified",
    "formal_ui",
    "r97b_modified",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "formal_apply",
]


def add(checks, name, passed, detail=None):
    item = {"check": name, "passed": bool(passed)}
    if detail is not None:
        item["detail"] = detail
    checks.append(item)


def load_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def main():
    checks = []

    for name in REQUIRED_FILES:
        add(checks, f"required_file:{name}", (ROOT / name).exists())

    manifest = load_json("PACKAGE_MANIFEST.json")
    schema = load_json("R223P_5_classroom_event_schema_v0_2_candidate.json")

    add(checks, "manifest_stage", manifest.get("stage_id") == "1013R_R223P_5_V0_2_LOCK_CANDIDATE")
    add(checks, "schema_status", schema.get("status") == "candidate_locked_not_published")
    add(checks, "decision", schema.get("decision") == "PASS_LOCK_R223M_STANDARD_V0_2_CANDIDATE")

    for flag in FORBIDDEN_TRUE_FLAGS:
        add(checks, f"boundary_false:{flag}", manifest.get(flag) is False)
    add(checks, "schema_v0_2_not_published_schema", schema.get("schema_v0_2_published") is False)
    add(checks, "formal_apply_false_schema", schema.get("formal_apply_allowed") is False)

    general_ids = {field.get("field_id") for field in schema.get("general_pedagogy_core_candidate_fields", [])}
    art_ids = {field.get("field_id") for field in schema.get("art_subject_adapter_candidate_fields", [])}
    ledger_ids = set(schema.get("review_ledger_only_fields", []))

    for field in GENERAL_FIELDS:
        add(checks, f"general_field:{field}", field in general_ids)
    for field in ART_FIELDS:
        add(checks, f"art_field:{field}", field in art_ids)
    for field in LEDGER_FIELDS:
        add(checks, f"ledger_field:{field}", field in ledger_ids)

    rules = "\n".join(schema.get("validator_candidate_rules", []))
    for term in [
        "demonstration_type",
        "micro_practice_type",
        "appreciation_scaffold_type",
        "material_experiment",
        "practice_creation",
        "showcase_evaluation",
        "teacher default view",
        "unit_phase_role",
        "practice_intensity",
    ]:
        add(checks, f"validator_rule_mentions:{term}", term in rules)

    for name in [
        "R223P_5_field_required_optional_ledger_only_policy.md",
        "R223P_5_general_core_vs_art_adapter_boundary.md",
        "R223P_5_unit_lesson_practice_intensity_router_contract.md",
        "R223P_5_teacher_default_view_guardrails.md",
        "R223P_5_review_ledger_requirements.md",
        "R223P_5_component_trigger_status_policy_lock.md",
        "R223P_5_regression_summary_from_P4.md",
        "R223P_5_next_stage_handoff.md",
    ]:
        text = read(name)
        add(checks, f"doc_has_not_published_or_blocked:{name}", "NOT_PUBLISHED" in text or "BLOCKED" in text or "not_published" in text or "不得" in text)

    guardrails = read("R223P_5_teacher_default_view_guardrails.md")
    for term in [
        "practice_pattern_type",
        "demonstration_type",
        "micro_practice_type",
        "component_trigger_status",
    ]:
        add(checks, f"guardrail_forbids:{term}", term in guardrails)

    router = read("R223P_5_unit_lesson_practice_intensity_router_contract.md")
    for sample in ["我为文具代言", "有趣的纸印", "色彩的碰撞"]:
        add(checks, f"router_regression_sample:{sample}", sample in router)

    component = read("R223P_5_component_trigger_status_policy_lock.md")
    for status in [
        "already_registered",
        "candidate_from_R222D_pool",
        "new_surface_candidate",
        "unregistered_do_not_execute",
    ]:
        add(checks, f"component_status:{status}", status in component)

    report = read("R223P_5_v0_2_candidate_lock_report.md")
    add(checks, "report_candidate_not_publish", "候选标准封存，不是正式发布" in report)

    failures = [check for check in checks if not check["passed"]]
    result = {
        "passed": not failures,
        "check_count": len(checks),
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_LOCK_R223M_STANDARD_V0_2_CANDIDATE" if not failures else "HOLD_FOR_P4_REGRESSION_RECHECK",
        "checks": checks,
    }
    (ROOT / "validate_1013R_R223P_5_v0_2_lock_candidate_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({k: result[k] for k in ["passed", "check_count", "failed", "decision"]}, ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
