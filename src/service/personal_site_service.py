import smtplib
from flask import jsonify, abort

from src.util.constants import *


def email_processor(data):
    try:
        email = data.get(EMAIL)
        with open("letter_template.txt") as letter_file:
            template = letter_file.read()

        formatted_content = template.format(**data)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(SENDER_EMAIL, SENDER_PASSWORD)
            connection.sendmail(from_addr=email, to_addrs=MY_EMAIL, msg=formatted_content)

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as error:
        abort(500, f"{error}")
