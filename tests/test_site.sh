#!/usr/bin/env bash
set -euo pipefail
for f in index.html about.html add-expense.html contact.html features.html help.html login.html privacy.html signup.html stories.html terms.html main.css script.js expense.js; do
  test -f "$f" || { echo "FAIL: missing $f"; exit 1; }
  echo "ok: $f present"
done
grep -qi "<html" index.html || { echo "FAIL: index.html is not HTML"; exit 1; }
grep -qi "Spendly" index.html || { echo "FAIL: index.html does not look like the Spendly site"; exit 1; }
test -s main.css || { echo "FAIL: main.css empty"; exit 1; }
test -s script.js || { echo "FAIL: script.js empty"; exit 1; }
test -s expense.js || { echo "FAIL: expense.js empty"; exit 1; }
echo "All site checks passed."
