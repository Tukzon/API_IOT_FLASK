from services.db import get_db_connection
from services.tools import api_key_gen
from flask import Blueprint, request, jsonify

ct_company = Blueprint('ct_company', __name__)

def new_company():
    conn = get_db_connection()
    cursor = conn.cursor()
    api_key = api_key_gen()
    company_data = request.get_json()
    cursor.execute("""INSERT INTO company (company_name, company_api_key) VALUES (?, ?)""", (company_data['company_name'], api_key))
    conn.commit()
    conn.close()
    return jsonify({"message": "Company created", "COMPANY_API_KEY": api_key, "status": 201})