from flask import Blueprint, request, jsonify
from services.db import get_db_connection

sensor_bp = Blueprint('sensor_bp', __name__)

@sensor_bp.route('/api/v1/sensors', methods=['GET'])
def get_all_sensors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sensors""")
    sensors = cursor.fetchall()
    conn.close()

    all_sensors = []
    for sensor in sensors:
        new_sensor = {
            "sensor_id": sensor[0],
            "sensor_name": sensor[1],
            "sensor_category": sensor[2],
            "sensor_meta": sensor[3],
            "sensor_api_key": sensor[4]
        }
        all_sensors.append(new_sensor)

    return jsonify(all_sensors), 200

@sensor_bp.route('/api/v1/sensors/<int:sensor_id>', methods=['GET'])
def get_one_sensor(sensor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sensors WHERE sensor_id = ?""", (sensor_id,))
    sensor = cursor.fetchone()
    conn.close()

    if sensor is not None:
        new_sensor = {
            "sensor_id": sensor[0],
            "sensor_name": sensor[1],
            "sensor_category": sensor[2],
            "sensor_meta": sensor[3],
            "sensor_api_key": sensor[4]
        }
        return jsonify(new_sensor), 200
    else:
        return "Sensor not found", 404
    
@sensor_bp.route('/api/v1/sensors/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sensors WHERE sensor_id = ?""", (sensor_id,))
    sensor = cursor.fetchone()
    if sensor is not None:
        sensor_data = request.get_json()
        cursor.execute("""UPDATE sensors SET sensor_name = ?, sensor_category = ?, sensor_meta = ?, sensor_api_key = ? WHERE sensor_id = ?""", (sensor_data['sensor_name'], sensor_data['sensor_category'], sensor_data['sensor_meta'], sensor_data['sensor_api_key'], sensor_id))
        conn.commit()
        conn.close()
        return "Sensor updated successfully", 200
    else:
        return "Sensor not found", 404
    
@sensor_bp.route('/api/v1/sensors/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sensors WHERE sensor_id = ?""", (sensor_id,))
    sensor = cursor.fetchone()
    if sensor is not None:
        cursor.execute("""DELETE FROM sensors WHERE sensor_id = ?""", (sensor_id,))
        conn.commit()
        conn.close()
        return "Sensor deleted successfully", 200
    else:
        return "Sensor not found", 404