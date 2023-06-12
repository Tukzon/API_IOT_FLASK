from services.db import get_db_connection
from services.tools import hash
from flask import Blueprint, request, jsonify

ct_admin = Blueprint('ct_admin', __name__)

def new_admin():
    conn = get_db_connection()
    cursor = conn.cursor()
    admin_data = request.get_json()
    password = hash(admin_data['password'])
    cursor.execute("""INSERT INTO admin (username, password) VALUES (?, ?)""", (admin_data['username'], password))
    conn.commit()
    conn.close()
    return jsonify({"message": "Admin Account created", "status": 201})