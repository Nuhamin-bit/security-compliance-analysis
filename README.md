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
├── control_mapping.csv     # Common finding types mapped to NIST, HIPAA, GDPR, PCI DSS
└── report/
    └── TEMPLATE.md         # Findings and remediation report template
```

## Method

1. **Scope and permission.** Define the lab systems in scope and confirm written authorization.
2. **Discovery.** Run an Nmap service and version scan (`scripts/scan.sh`).
3. **Host checks.** Use Bash on Linux and built-in tools on Windows to check accounts, permissions, services and logging.
4. **Parse results.** Convert scan output to a table (`scripts/parse_nmap.py`).
5. **Map to controls.** Match each finding to the relevant controls (`control_mapping.csv`).
6. **Report.** Rate severity, recommend fixes and summarize for non-technical readers (`report/TEMPLATE.md`).

## Lab environment

- **Attack machine:** Kali Linux virtual machine in Oracle VirtualBox, on an isolated virtual (NAT) network
- **Targets:** hosts on that virtual network (gateway, DNS service and my own VM), one Windows 11 device I own on my home network, and public practice domains built for training
- **Tools:** Nmap, Nessus Essentials, Fping, Hping3, Tcpdump, dig, netcat and Bash

## What I assessed

| Assessment | What I did |
|---|---|
| **Network discovery and port scanning** | SYN scans, targeted port scans and default script scans with Nmap; ping sweeps with Fping; crafted SYN, ACK and FIN packets with Hping3 while capturing traffic in Tcpdump |
| **Vulnerability scanning** | Nessus Essentials Basic Network Scan of a Windows 11 host, with research on each finding and its CVE status |
| **Footprinting (reconnaissance)** | WHOIS and DNS lookups, HTTP banner grabbing with netcat, cookie and web-beacon analysis, and a DNS zone transfer test against a practice domain |
| **Linux host hardening** | Users, groups and file permissions (least-privilege `chmod` settings), process control and log-friendly command-line administration |
| **Scripting** | A Bash script to generate IP address ranges for scanning, debugged line by line |

## Findings summary

| # | Finding | System | Severity | Main controls affected | Fix |
|---|---|---|---|---|---|
| 1 | **SSL certificate cannot be trusted** (self-signed). Nessus plugin 51192, CVSS v3 6.5. No CVE: a configuration weakness, not a software bug. Enables impersonation (man-in-the-middle). | Windows 11 host | Medium | NIST SC-17 PKI Certificates; CSF PR.DS-02; HIPAA 164.312(e)(1); GDPR Art. 32; PCI DSS 4.2.1 | Replace with a certificate from a trusted public or internal certificate authority, and install the full certificate chain |
| 2 | **DNS zone transfer allowed to anyone** (AXFR). One `dig` command downloaded the full zone: internal host names, office locations, an outdated Windows XP host, a staff contact and GPS coordinates. | Practice domain (zonetransfer.me) | High (in a real organization) | NIST CM-7 Least Functionality, AC-3 Access Enforcement; CSF PR.PS-01; HIPAA 164.308(a)(1)(ii)(B); GDPR Art. 32; PCI DSS 2.2.1 | Allow zone transfers only to approved secondary servers, authenticated with TSIG keys; keep internal names and staff details out of public DNS |
| 3 | **Public registration records expose named staff** (names, emails, direct phone numbers), useful for phishing and help-desk impersonation. | Public domain records (footprinting exercise) | Low | NIST AT-2 Awareness Training; CSF PR.AT-01; HIPAA 164.308(a)(5); GDPR Art. 32; PCI DSS 12.6.3.1 | Use role-based contacts (for example, noc@ or security@) instead of named people; train staff on social engineering |
| 4 | **Windows file sharing and RPC exposed** (ports 445 and 135). SMB v3.1.1 with message signing *required*, which is a good control against relay attacks. | Virtual network gateway | Informational | NIST CM-7; CSF PR.PS-01; PCI DSS 2.2.4 | Keep signing required; expose SMB and RPC only where needed |

**Positive result:** my own Kali VM showed all 1,000 common ports filtered, with no services exposed. No web (80/443) or email (25) services were running anywhere in the range.

**Main takeaway:** most scanner output is informational (25 of 26 Nessus items). The skill is separating real risk from noise and explaining it in the compliance language each team uses.

## Usage

```bash
# Scan an authorized lab target and save XML output
./scripts/scan.sh 192.168.56.10 results/target1

# Convert to CSV
python3 scripts/parse_nmap.py results/target1.xml results/target1.csv
```

## Ethics

Only scan systems you own or have **written permission** to test. Scanning systems without permission may be illegal. All work in this project was done on my own virtual lab, a device I own, and public practice domains built for training. No real IP addresses are published here.

## Author

**Nuhamin H. Tesfay** · M.S. Cybersecurity, Marymount University · [LinkedIn](https://www.linkedin.com/in/nuhamintesfay)
