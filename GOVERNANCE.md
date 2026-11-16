# 🏛️ Project Governance

## Project ownership

The repository identifies its maintainer and review owner through the GitHub repository settings and CODEOWNERS file. The maintainer is responsible for reviewing changes, managing releases, and coordinating security reports.

## Decision process

- Small fixes may be proposed through focused pull requests.
- Larger product or architecture changes should begin with an issue or feature proposal.
- Changes affecting datasets, derived model artifacts, privacy, or licensing require explicit provenance and rights review.
- Security vulnerabilities must be reported privately using SECURITY.md.
- Decisions should record meaningful alternatives and trade-offs in an Architecture Decision Record when they affect long-term design.

## Contribution and review

Contributors should follow CONTRIBUTING.md, the Code of Conduct, and the pull request template. Reviewers should consider correctness, compatibility, privacy, security, accessibility, test evidence, and documentation impact.

## Releases

A release should identify the source commit and the matching model artifact build. The four pickle artifacts must be treated as one compatible set. Follow docs/release-process.md and the deployment checklist.

## Changes to governance

Propose changes through a documented issue or pull request. This file describes the current lightweight maintainer-led process; it does not imply a formal committee or guaranteed review timeline.