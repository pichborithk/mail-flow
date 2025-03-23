import smtplib
from email.message import EmailMessage
from flask import jsonify, abort

from src.util.constants import *


def email_processor(data):
    try:
        # Create email
        msg = EmailMessage()
        msg["Subject"] = data.get(SUBJECT)
        msg["From"] = SENDER_EMAIL
        msg["To"] = MY_EMAIL
        msg["Reply-To"] = data.get(EMAIL)

        # Email body
        with open("letter_template.txt") as letter_file:
            template = letter_file.read()

        formatted_content = template.format(**data)
        msg.set_content(formatted_content)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(SENDER_EMAIL, SENDER_PASSWORD)
            connection.send_message(msg)
            connection.quit()

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as error:
        abort(500, f"{error}")
