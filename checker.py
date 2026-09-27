"""
Password Strength Checker - Core Logic
Task 2 | CyberSecurity Track | AVIP 2026

Rule set (documented, configurable via THRESHOLDS below):
    +2 points  length >= 12
    +1 point   length >= 8  (and < 12)
    +1 point   contains lowercase letter
    +1 point   contains uppercase letter
    +1 point   contains digit
    +1 point   contains special character (!@#$%^&*()-_+=... etc.)
    -1 point   password is in the common/weak password blocklist
    -1 point   length < 6 (hard penalty, very short passwords)

Score -> Category thresholds (edit THRESHOLDS to reconfigure):
    score <= 1              -> Weak
    2 <= score <= 3         -> Moderate
    score >= 4              -> Strong
"""

import re
import string

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "letmein", "admin", "welcome",
}

THRESHOLDS = {
    "weak_max": 1,       # score <= this -> Weak
    "moderate_max": 3,   # score <= this (and > weak_max) -> Moderate
    # score > moderate_max -> Strong
}

SPECIAL_CHARS = string.punctuation


def check_password(password: str) -> dict:
    """Return a dict with score, category, and a rationale list."""
    reasons = []
    score = 0

    length = len(password)

    if length >= 12:
        score += 2
        reasons.append("+2: length is 12+ characters")
    elif length >= 8:
        score += 1
        reasons.append("+1: length is 8-11 characters")
    else:
        reasons.append("+0: length is under 8 characters")

    if length < 6:
        score -= 1
        reasons.append("-1: password is very short (<6 chars)")

    if re.search(r"[a-z]", password):
        score += 1
        reasons.append("+1: contains lowercase letter")
    else:
        reasons.append("+0: no lowercase letter")

    if re.search(r"[A-Z]", password):
        score += 1
        reasons.append("+1: contains uppercase letter")
    else:
        reasons.append("+0: no uppercase letter")

    if re.search(r"[0-9]", password):
        score += 1
        reasons.append("+1: contains a digit")
    else:
        reasons.append("+0: no digit")

    if any(ch in SPECIAL_CHARS for ch in password):
        score += 1
        reasons.append("+1: contains a special character")
    else:
        reasons.append("+0: no special character")

    if password.lower() in COMMON_PASSWORDS:
        score -= 1
        reasons.append("-1: found in common/weak password list")

    if score <= THRESHOLDS["weak_max"]:
        category = "Weak"
    elif score <= THRESHOLDS["moderate_max"]:
        category = "Moderate"
    else:
        category = "Strong"

    return {"password": password, "score": score, "category": category, "reasons": reasons}


if __name__ == "__main__":
    import sys
    pw = sys.argv[1] if len(sys.argv) > 1 else input("Enter password to check: ")
    result = check_password(pw)
    print(f"\nPassword: {result['password']}")
    print(f"Score: {result['score']}")
    print(f"Category: {result['category']}")
    print("Rationale:")
    for r in result["reasons"]:
        print(f"  {r}")
