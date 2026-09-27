# CS_2_PasswordChecker_byte

Password Strength Checker — Web App + CLI
**AVIP 2026 | CyberSecurity Track | Task 2**

## What it does
Scores a password and returns a category — **Weak / Moderate / Strong** —
with a plain-English rationale. Available as both a CLI script and a Flask
web app (deployable live on Render).

## Files
| File | Purpose |
|---|---|
| `checker.py` | Core scoring logic (framework-independent) — also runnable as CLI |
| `app.py` | Flask web app |
| `templates/index.html` | Web UI |
| `requirements.txt` | Dependencies for deployment |
| `test_cases.py` | 7 documented test cases (weak/moderate/strong) |
| `sample_run.txt` | Captured output of running `test_cases.py` |

## Rule set (documented & configurable)
| Rule | Points |
|---|---|
| Length ≥ 12 | +2 |
| Length 8–11 | +1 |
| Length < 6 | −1 (hard penalty) |
| Contains lowercase letter | +1 |
| Contains uppercase letter | +1 |
| Contains digit | +1 |
| Contains special character | +1 |
| In common/weak password list | −1 |

**Thresholds** (edit `THRESHOLDS` dict in `checker.py` to reconfigure):
- Score ≤ 1 → **Weak**
- Score 2–3 → **Moderate**
- Score ≥ 4 → **Strong**

## Run locally

CLI:
```bash
python checker.py "MyP@ssw0rd!"
```

Web app:
```bash
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000
```

Run test suite:
```bash
python test_cases.py
```

## Deploy live (Render.com — free)
1. Push this repo to GitHub (public).
2. Go to [render.com](https://render.com) → New → **Web Service** → connect your GitHub repo.
3. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Click **Deploy**. Render gives you a live URL like `https://cs-2-passwordchecker-byte.onrender.com`.
5. Use that URL as your live demo link.

## Sample test results
See `sample_run.txt` — all 7/7 test cases pass (mix of common passwords,
short passwords, and strong mixed-character passwords).

## Tech stack
Python 3, Flask, Gunicorn (production server for deployment).
