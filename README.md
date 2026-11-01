# Security Governance & Compliance Analysis

**From scan results to compliance language.** This project runs vulnerability assessments on Linux and Windows systems and maps each finding to the controls in **NIST**, **HIPAA**, **GDPR** and **PCI DSS**, so technical results can be reported in terms that compliance teams and leadership understand.

## Why it matters

A port scan tells an engineer what is open. A compliance team needs to know which requirement is at risk and what to fix first. This project bridges that gap.

## What's inside

```
security-compliance-analysis/
├── scripts/
│   ├── scan.sh             # Nmap service scan of an authorized target (saves XML)
│   └── parse_nmap.py       # Turns Nmap XML into a CSV of open ports and services
├── mapping/
│   └── control_mapping.csv # Common finding types mapped to NIST, HIPAA, GDPR, PCI DSS
└── report/
    └── TEMPLATE.md         # Findings and remediation report template
```

## Method

1. **Scope and permission.** Define the lab systems in scope and confirm written authorization.
2. **Discovery.** Run an Nmap service and version scan (`scripts/scan.sh`).
3. **Host checks.** Use Bash on Linux and built-in tools on Windows to check accounts, permissions, services and logging.
4. **Parse results.** Convert scan output to a table (`scripts/parse_nmap.py`).
5. **Map to controls.** Match each finding to the relevant controls (`mapping/control_mapping.csv`).
6. **Report.** Rate severity, recommend fixes and summarize for non-technical readers (`report/TEMPLATE.md`).

## Lab environment

<!-- TO FILL IN: describe your lab, for example "Ubuntu 22.04 and Windows Server 2019 virtual machines on an isolated network." -->

## Findings summary

<!-- TO FILL IN from your assessment. Do not include real IP addresses or sensitive details. -->

| # | Finding | System | Severity | Main control affected | Fix |
|---|---|---|---|---|---|
| 1 | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

## Usage

```bash
# Scan an authorized lab target and save XML output
./scripts/scan.sh 192.168.56.10 results/target1

# Convert to CSV
python3 scripts/parse_nmap.py results/target1.xml results/target1.csv
```

## Ethics

Only scan systems you own or have **written permission** to test. Scanning systems without permission may be illegal. All work in this project was done in a lab environment.

## Author

**Nuhamin H. Tesfay** · M.S. Cybersecurity, Marymount University · [LinkedIn](https://www.linkedin.com/in/nuhamintesfay)
