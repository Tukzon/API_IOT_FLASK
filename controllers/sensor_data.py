from services.db import get_db_connection
from flask import Blueprint, request, jsonify
import time

ct_sensor_data = Blueprint('ct_sensor_data', __name__)

def get_data(sensor_api_key, from_timestamp, to_timestamp):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM sensor_data, sensor WHERE sensor_data.sensor_id = sensor.sensor_id AND sensor.sensor_api_key = %s AND sensor_data.sensor_data_timestamp BETWEEN %s AND %s', (sensor_api_key, from_timestamp, to_timestamp))
    data = cursor.fetchall()
    db.close()
    return jsonify(data, 200)


def create_data():
    db = get_db_connection()
    current_time = time.time()
    sensor_data = request.get_json()
    cursor = db.cursor()
    for variable in sensor_data['sensor_data']:
        cursor.execute('INSERT INTO sensor_data (sensor_data_variable, sensor_data_value, sensor_data_timestamp, sensor_id) VALUES (%s, %s, %s, %s)', (variable['nombre'], variable['valor'], current_time, sensor_data['sensor_id']))
    db.commit()
    db.close()
    return jsonify({"message": "Data created", "status": 201})