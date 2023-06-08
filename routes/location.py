from flask import Blueprint,jsonify, request

from controllers import location

location_bp = Blueprint('location_bp', __name__)

@location_bp.route('/api/v1/location', methods=['GET'])
def get_all_locations():
    return location.get_locations(), 200

@location_bp.route('/api/v1/location/<int:location_id>', methods=['GET'])
def get_one_location(location_id):
    return location.get_location_by_id(location_id), 200
        
    
@location_bp.route('/api/v1/location/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    return location.update_location_by_id(location_id), 200
    
@location_bp.route('/api/v1/location/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    return location.delete_location_by_id(location_id), 200