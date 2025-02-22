from flask import Flask, request, render_template, jsonify
import smtplib

app = Flask(__name__)

# Replace with your email credentials
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"
RECEIVER_EMAIL = "koresco4@gmail.com"

@app.route("/")
def home():
    return render_template("index.html")  # Ensure your HTML file is named "index.html"

@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Sending the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            subject = "New Subscription"
            body = f"New subscriber: {email}"
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, msg)
        return jsonify({"success": "Subscription received!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
