from services.db import get_db_connection
from services.tools import string_a_lista
from flask import Blueprint, request, jsonify
import time

ct_sensor_data = Blueprint('ct_sensor_data', __name__)

import json

def get_data(sensor_api_key, from_timestamp, to_timestamp, sensor_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM sensor WHERE sensor_api_key = ?', (sensor_api_key,))
    sensor_verify = cursor.fetchone()
    if sensor_verify is None:
        db.close()
        return jsonify({"message": "Sensor not found", "status": 400})
    
    sensores = string_a_lista(sensor_id)
    query = 'SELECT * FROM sensor_data, sensor WHERE sensor_data.sensor_id = sensor.sensor_id AND sensor.sensor_api_key = ? AND sensor_data.sensor_data_timestamp BETWEEN ? AND ?'
    params = (sensor_api_key, from_timestamp, to_timestamp)
    
    if len(sensores) > 0:
        placeholders = ', '.join(['?'] * len(sensores))
        query += f' AND sensor_data.sensor_id IN ({placeholders})'
        params += tuple(sensores)
    
    cursor.execute(query, params)
    rows = cursor.fetchall()

    data = [dict(row) for row in rows]
    
    db.close()
    
    return jsonify(data, 200)




def create_data():
    db = get_db_connection()
    sensor_data = request.get_json()
    cursor = db.cursor()
    cursor.execute('SELECT sensor_id FROM sensor WHERE sensor_api_key = ?', (sensor_data['sensor_api_key'],))
    sensor = cursor.fetchone()
    if sensor is None:
        return jsonify({"message": "Sensor not found", "status": 400})
    sensor_id = sensor[0]
    for variable in sensor_data['json_data']:
        current_time = time.time()
        cursor.execute('INSERT INTO sensor_data (sensor_data_variable, sensor_data_value, sensor_data_timestamp, sensor_id) VALUES (?, ?, ?, ?)', (variable['nombre'], variable['valor'], current_time, sensor_id))
    db.commit()
    db.close()
    return jsonify({"message": "Data created", "status": 201})