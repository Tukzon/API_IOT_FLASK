from services.db import get_db_connection
from services.api_key_gen import api_key_gen
from flask import Blueprint, request, jsonify

ct_sensor = Blueprint('ct_sensor', __name__)

def new_sensor():
    conn = get_db_connection()
    cursor = conn.cursor()
    api_key = api_key_gen()
    sensor_data = request.get_json()
    cursor.execute("""INSERT INTO sensor (location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?)""", (sensor_data['location_id'], sensor_data['sensor_name'], sensor_data['sensor_category'], sensor_data['sensor_meta'], api_key))
    conn.commit()
    conn.close()
    return jsonify({"message": "Sensor created", "SENSOR_API_KEY": api_key, "status": 201})

def get_sensors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sensor""")
    sensors = cursor.fetchall()
    conn.close()

    all_sensors = []
    for sensor in sensors:
        new_sensor = {
            "location_id": sensor[0],
            "sensor_id": sensor[1],
            "sensor_name": sensor[2],
            "sensor_category": sensor[3],
            "sensor_meta": sensor[4],
            "sensor_api_key": sensor[5]
        }
        all_sensors.append(new_sensor)

    if len(all_sensors) == 0:
        return jsonify({"message": "No sensors found", "status": 404})

    return jsonify(all_sensors, 200)

def get_sensor_by_api_key(sensor_api_key):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sensor WHERE sensor_api_key = ?""", (sensor_api_key,))
    sensor = cursor.fetchone()
    conn.close()

    if sensor is not None:
        sensor = {
            "location_id": sensor[0],
            "sensor_id": sensor[1],
            "sensor_name": sensor[2],
            "sensor_category": sensor[3],
            "sensor_meta": sensor[4],
        }
        return jsonify(sensor, 200)
    else:
        return jsonify({"message": "Sensor not found", "status": 404})
    
def update_sensor_by_api_key(sensor_api_key):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sensor WHERE sensor_api_key = ?""", (sensor_api_key,))
    sensor = cursor.fetchone()
    if sensor is not None:
        sensor_data = request.get_json()
        cursor.execute("""UPDATE sensor SET sensor_name = ?, sensor_category = ?, sensor_meta = ?, location_id = ? WHERE sensor_api_key = ?""", (sensor_data['sensor_name'], sensor_data['sensor_category'], sensor_data['sensor_meta'], sensor_data['location_id'], sensor_api_key))
        conn.commit()
        conn.close()
        return jsonify({"message": "Sensor updated", "status": 200})
    else:
        conn.close()
        return jsonify({"message": "Sensor not found", "status": 404})
    
def delete_sensor_by_api_key(sensor_api_key):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sensor WHERE sensor_api_key = ?""", (sensor_api_key,))
    sensor = cursor.fetchone()
    if sensor is not None:
        cursor.execute("""DELETE FROM sensor WHERE sensor_api_key = ?""", (sensor_api_key,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Sensor deleted", "status": 200})
    else:
        conn.close()
        return jsonify({"message": "Sensor not found", "status": 404})