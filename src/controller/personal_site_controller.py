from flask import request

from src import app
from src.service import personal_site_service


@app.post("/api/personal-site")
def personal_site_mail():
    return personal_site_service.email_processor(request.get_json())
