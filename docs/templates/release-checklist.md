# 🚀 Release Checklist

## Code and dependencies
- [ ] Change reviewed
- [ ] Python syntax check passed
- [ ] Runtime and development dependency installation verified
- [ ] No secrets or personal data added
- [ ] Dependency changes reviewed for compatibility and security

## Data and model
- [ ] Dataset source and permitted use reviewed
- [ ] Only trusted artifacts are used
- [ ] All four pickle files come from one model build
- [ ] Artifact checksums and build identifier recorded
- [ ] Pivot index and similarity matrix row alignment validated
- [ ] Model evaluation protocol and results recorded if claims are made

## Application behavior
- [ ] Home page smoke-tested
- [ ] Recommendation form smoke-tested
- [ ] Known-title recommendation tested
- [ ] Blank and unknown title behavior checked
- [ ] Debug mode disabled in production
- [ ] WSGI startup verified

## Security, privacy, and accessibility
- [ ] Security findings reviewed
- [ ] Sensitive data minimized
- [ ] Remote image behavior documented
- [ ] Keyboard and focus review completed
- [ ] Form labels and validation reviewed
- [ ] Contrast and zoom checks recorded

## Operations
- [ ] Deployment revision recorded
- [ ] Backup available
- [ ] Rollback plan documented
- [ ] Monitoring configured at hosting layer
- [ ] Release notes and documentation updated

## Approval
- Release owner:
- Commit:
- Model build:
- Date:
- Known exceptions:
