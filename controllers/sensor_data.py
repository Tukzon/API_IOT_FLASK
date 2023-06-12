from services.db import get_db_connection
from services.tools import string_a_lista
from flask import Blueprint, request, jsonify
import time

ct_sensor_data = Blueprint('ct_sensor_data', __name__)

import json

def get_data(company_api_key, from_timestamp, to_timestamp, sensor_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM company WHERE company_api_key = ?', (company_api_key,))
    company_verify = cursor.fetchone()
    if company_verify is None:
        db.close()
        return jsonify({"message": "API KEY NOT VALID", "status": 401})

    sensores = string_a_lista(sensor_id)
    if not sensores:
        db.close()
        return jsonify({"message": "No valid sensor IDs provided", "status": 400})
    
    # Verificar si los sensores existen en la base de datos
    placeholders = ', '.join(['?'] * len(sensores))
    query = 'SELECT sensor_id FROM sensor WHERE sensor_id IN ({})'.format(placeholders)
    cursor.execute(query, tuple(sensores))
    existing_sensors = cursor.fetchall()
    existing_sensor_ids = [row[0] for row in existing_sensors]
    
    # Verificar si algún sensor proporcionado no existe
    non_existing_sensors = [sensor for sensor in sensores if sensor not in existing_sensor_ids]
    if non_existing_sensors:
        db.close()
        return jsonify({"message": f"Non-existing sensor IDs: {non_existing_sensors}", "status": 400})
    
    query = '''
        SELECT * FROM sensor_data
        WHERE sensor_id IN ({}) AND sensor_data_timestamp BETWEEN ? AND ?
    '''.format(placeholders)
    params = sensores + [from_timestamp, to_timestamp]
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    if not rows:
        db.close()
        return jsonify({"message": "No data found for the specified filters", "status": 404})
    
    data = []
    for row in rows:
        data.append({
            "sensor_id": row[0],
            "sensor_data_id": row[1],
            "sensor_data_variable": row[2],
            "sensor_data_value": row[3],
            "sensor_data_timestamp": row[4]
        })
    
    db.close()
    
    return jsonify(data)


def get_full_data(dev_password):
    if dev_password != 'tukzon':
        return jsonify({"message": "NO TIENES PERMISOS PARA UTILIZAR ESTE ENDPOINT", "status": 400})
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM sensor_data')
    rows = cursor.fetchall()
    db.close()
    data = [dict(row) for row in rows]
    return jsonify(data)


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