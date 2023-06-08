from services.db import get_db_connection
from services.api_key_gen import api_key_gen
from flask import Blueprint, request, jsonify

ct_sensor = Blueprint('ct_sensor', __name__)

def new_sensor():
    conn = get_db_connection()
    cursor = conn.cursor()
    api_key = api_key_gen()
    sensor_data = request.get_json()
    cursor.execute("""INSERT INTO sensor (location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?, ?)""", (sensor_data['location_id'], sensor_data['sensor_id'], sensor_data['sensor_name'], sensor_data['sensor_category'], sensor_data['sensor_meta'], api_key))
    conn.commit()
    conn.close()
    return jsonify({"message": "Sensor created", "SENSOR_API_KEY": api_key, "status": 201})