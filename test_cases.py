"""
Test cases for Password Strength Checker.
Run: python test_cases.py
"""

from checker import check_password

TEST_CASES = [
    # (password, expected_category)
    ("123456", "Weak"),            # common password, all-digit, short
    ("password", "Weak"),          # common password, no digits/upper/special
    ("a", "Weak"),                 # very short
    ("abcdefgh", "Moderate"),      # lowercase only, 8 chars
    ("Abcdef12", "Strong"),        # mixed case + digits, 8 chars
    ("MyP@ssw0rd!", "Strong"),     # long, mixed case, digit, special char
    ("Tr0ub4dor&3xyz", "Strong"),  # long, all character classes
]

if __name__ == "__main__":
    passed = 0
    for pw, expected in TEST_CASES:
        result = check_password(pw)
        status = "PASS" if result["category"] == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"[{status}] '{pw}' -> got={result['category']} (score={result['score']}), expected={expected}")

    print(f"\n{passed}/{len(TEST_CASES)} test cases passed.")
