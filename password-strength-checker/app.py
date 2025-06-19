from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Final feedback
    if score == 5:
        return "Strong password!", []
    elif score >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    suggestions = []
    password = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        strength, suggestions = check_password_strength(password)
    return render_template('index.html', strength=strength, suggestions=suggestions, password=password)

if __name__ == "__main__":
    app.run(debug=True)