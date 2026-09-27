"""
Password Strength Checker - Flask Web App
Task 2 | CyberSecurity Track | AVIP 2026

Run locally:  python app.py
Deploy live:  see README.md (Render.com instructions)
"""

from flask import Flask, render_template, request
from checker import check_password

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form.get("password", "")
        if password:
            result = check_password(password)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
