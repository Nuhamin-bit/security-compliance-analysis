#!/usr/bin/env python3
"""Convert Nmap XML output into a CSV of open ports and services.

Usage: python3 parse_nmap.py <nmap.xml> <output.csv>
"""
import csv
import sys
import xml.etree.ElementTree as ET


def parse(xml_path):
    rows = []
    root = ET.parse(xml_path).getroot()
    for host in root.findall("host"):
        addr = host.find("address")
        ip = addr.get("addr") if addr is not None else ""
        for port in host.findall("./ports/port"):
            state = port.find("state")
            if state is None or state.get("state") != "open":
                continue
            svc = port.find("service")
            rows.append({
                "host": ip,
                "port": port.get("portid"),
                "protocol": port.get("protocol"),
                "service": svc.get("name", "") if svc is not None else "",
                "product": svc.get("product", "") if svc is not None else "",
                "version": svc.get("version", "") if svc is not None else "",
            })
    return rows


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    rows = parse(sys.argv[1])
    fields = ["host", "port", "protocol", "service", "product", "version"]
    with open(sys.argv[2], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} open ports to {sys.argv[2]}")


if __name__ == "__main__":
    main()
