from services.db import get_db_connection
from flask import Flask, request, jsonify


def get_locations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM location""")
    locations = cursor.fetchall()
    conn.close()

    all_locations = []
    for location in locations:
        new_location = {
            "location_id": location[0],
            "sensor_id": location[1],
            "sensor_name": location[2],
            "sensor_category": location[3],
            "sensor_meta": location[4],
            "sensor_api_key": location[5]
        }
        all_locations.append(new_location)
    return all_locations

def get_location_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM location WHERE location_id = ?""", (id,))
    location = cursor.fetchone()
    conn.close()

    if location is not None:
        new_location = {
            "location_id": location[0],
            "sensor_id": location[1],
            "sensor_name": location[2],
            "sensor_category": location[3],
            "sensor_meta": location[4],
            "sensor_api_key": location[5]
        }
        return new_location
    else:
        return "Location not found", 404
    
def update_location_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM location WHERE location_id = ?""", (id,))
    location = cursor.fetchone()
    if location is not None:
        location_data = request.get_json()
        cursor.execute("""UPDATE location SET sensor_id = ?, sensor_name = ?, sensor_category = ?, sensor_meta = ?, sensor_api_key = ? WHERE location_id = ?""", (location_data['sensor_id'], location_data['sensor_name'], location_data['sensor_category'], location_data['sensor_meta'], location_data['sensor_api_key'], id))
        conn.commit()
        conn.close()
        return True
    else:
        return False
    
def delete_location_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM location WHERE location_id = ?""", (id,))
    location = cursor.fetchone()
    if location is not None:
        cursor.execute("""DELETE FROM location WHERE location_id = ?""", (id,))
        conn.commit()
        conn.close()
        return True
    else:
        return False