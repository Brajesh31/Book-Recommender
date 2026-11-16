# 🧪 Test Plan: <change>

## Objective

What behavior or risk is this plan verifying?

## Scope

- Included routes, helpers, templates, model artifacts:
- Excluded areas:

## Environment

- Commit:
- Python version:
- OS:
- Dependency lock/revision:
- Artifact build ID:

## Scenarios

| ID | Scenario | Input/setup | Expected result | Evidence |
|---|---|---|---|---|
| T-01 | Home page | Valid artifact set | Popular page renders | |
| T-02 | Recommendation form | GET /recommend | Form renders | |
| T-03 | Known title | Exact index title | Candidate cards render | |
| T-04 | Empty title | Empty form field | Safe validation message | |
| T-05 | Unknown title | Missing title | No unhandled exception | |
| T-06 | Incompatible artifact | Wrong matrix rows | Startup fails safely | |

## Accessibility checks

- [ ] Keyboard-only navigation
- [ ] Visible focus
- [ ] Labels and error association
- [ ] Contrast
- [ ] 200% zoom
- [ ] Screen-reader announcement

## Results

Record pass/fail, logs, screenshots, skipped checks, and defects. Do not mark an unexecuted test as passed.

## Sign-off

- Tester:
- Date:
- Known issues:
