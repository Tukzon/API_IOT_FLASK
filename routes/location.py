from services.db import get_db_connection
from controllers.location import get_locations, get_location_by_id, update_location_by_id, delete_location_by_id
from flask import jsonify, request
from app import app


@app.route('/api/v1/location', methods=['GET'])
def get_all_locations():
    try:
        locations = get_locations()
        return jsonify(locations), 200
    except Exception as e:
        print(e)
        return "Internal Server Error", 500

@app.route('/api/v1/location/<int:location_id>', methods=['GET'])
def get_one_location(location_id):
    try:
        location = get_location_by_id(location_id)
        return jsonify(location), 200
    except Exception as e:
        print(e)
        return "Internal Server Error", 500
    
@app.route('/api/v1/location/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    try:
        update = update_location_by_id(location_id)
        return jsonify(update), 200
    except Exception as e:
        print(e)
        return "Internal Server Error", 500
    
@app.route('/api/v1/location/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    try:
        delete = delete_location_by_id(location_id)
        return jsonify(delete), 200
    except Exception as e:
        print(e)
        return "Internal Server Error", 500