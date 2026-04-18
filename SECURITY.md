# Security Policy

## 🛡️ Commitment
We take the security of `vtuber-contracts` seriously. This project aims for a **Medium** security standard.

## 📢 Reporting a Vulnerability
Please do not report security vulnerabilities through public GitHub issues. Instead, send a detailed report to:
**mr.bt1590@gmail.com**

### What to include:
- A description of the vulnerability.
- Steps to reproduce (PoC).
- Potential impact.

## 🔐 Security Protocols
This repo defines schemas only — no runtime secrets and no network surface. Treat any addition of fields containing tokens, API keys, or PII as a higher-tier review and document the field's threat model in DESIGN_DECISIONS.md before merge.

- **Dependency Management:** Regularly scan for vulnerable packages.
- **CI/CD Security:** Mandatory automated security scans are integrated into `.github/workflows/security.yml`.
- **Disclosure:** We follow a responsible disclosure timeline.
