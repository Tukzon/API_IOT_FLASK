from services.db import get_db_connection
from flask import Blueprint, request, jsonify

ct_location = Blueprint('ct_location', __name__)

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
            "company_id": location[1],
            "location_name": location[2],
            "location_county": location[3],
            "location_city": location[4],
            "location_meta": location[5]
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
            "company_id": location[1],
            "location_name": location[2],
            "location_county": location[3],
            "location_city": location[4],
            "location_meta": location[5]
        }
        return jsonify(new_location, 200)
    else:
        return jsonify({"message": "Location not found", "status": 404})
    
def create_location():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        location_data = request.get_json()
        cursor.execute("""SELECT * FROM company WHERE company_api_key = ?""", (location_data['company_api_key'],))
        company = cursor.fetchone()
        if company is None:
            return jsonify({"message": "API KEY NOT VALID", "status": 400})
        cursor.execute("""INSERT INTO location (company_id, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)""", (location_data['company_id'], location_data['location_name'], location_data['location_country'], location_data['location_city'], location_data['location_meta']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Location created", "status": 201})
    except:
        return jsonify({"message": "Something went wrong", "status": 500})
    
def update_location_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    location_data = request.get_json()
    cursor.execute("""SELECT * FROM company WHERE company_api_key = ?""", (location_data['company_api_key'],))
    company = cursor.fetchone()
    if company is None:
        return jsonify({"message": "API KEY NOT VALID", "status": 400})
    cursor.execute("""SELECT * FROM location WHERE company_id = ?""", (id,))
    location = cursor.fetchone()
    if location is not None:
        cursor.execute("""UPDATE location SET location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE company_id = ?""", (location_data['location_name'], location_data['location_country'], location_data['location_city'], location_data['location_meta'], id))
        conn.commit()
        conn.close()
        return jsonify({"message": "Location updated", "status": 200})
    else:
        return jsonify({"message": "YOU CANNOT UPDATE THIS LOCATION", "status": 404})
    
def delete_location_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    location_data = request.get_json()
    cursor.execute("""SELECT * FROM company WHERE company_api_key = ?""", (location_data['company_api_key'],))
    company = cursor.fetchone()
    if company is None:
        return jsonify({"message": "API KEY NOT VALID", "status": 400})
    cursor.execute("""SELECT * FROM location WHERE company_id = ?""", (id,))
    location = cursor.fetchone()
    if location is not None:
        cursor.execute("""DELETE FROM location WHERE company_id = ?""", (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Location deleted", "status": 200})
    else:
        return jsonify({"message": "YOU CANNOT DELETE THIS LOCATION", "status": 404})