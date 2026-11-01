#!/usr/bin/env bash
# Service and version scan of ONE authorized target. Saves Nmap XML output.
# Usage: ./scan.sh <target> <output-prefix>
# Only scan systems you own or have written permission to test.
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <target> <output-prefix>" >&2
  exit 1
fi

TARGET="$1"
OUT="$2"

read -r -p "Do you have written authorization to scan ${TARGET}? (yes/no) " ANSWER
if [ "${ANSWER}" != "yes" ]; then
  echo "Scan cancelled. Get written authorization first." >&2
  exit 1
fi

mkdir -p "$(dirname "${OUT}")"

# -sV: detect service versions; -T3: normal timing; top 1000 TCP ports by default
nmap -sV -T3 -oX "${OUT}.xml" -oN "${OUT}.txt" "${TARGET}"

echo "Saved ${OUT}.xml and ${OUT}.txt"
