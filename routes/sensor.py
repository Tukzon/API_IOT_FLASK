from flask import Blueprint, request, jsonify
from services.db import get_db_connection

from controllers import sensor

sensor_bp = Blueprint('sensor_bp', __name__)

@sensor_bp.route('/api/v1/sensor', methods=['POST'])
def create_sensor():
    return sensor.new_sensor(), 200

@sensor_bp.route('/api/v1/sensor', methods=['GET'])
def get_all_sensors():
    return sensor.get_sensors(), 200

@sensor_bp.route('/api/v1/sensor/<string:sensor_api_key>', methods=['GET'])
def get_one_sensor(sensor_api_key):
    return sensor.get_sensor_by_api_key(sensor_api_key), 200
    
@sensor_bp.route('/api/v1/sensor/<string:sensor_api_key>', methods=['PUT'])
def update_sensor(sensor_api_key):
    return sensor.update_sensor_by_api_key(sensor_api_key), 200
    
@sensor_bp.route('/api/v1/sensor/<string:sensor_api_key>', methods=['DELETE'])
def delete_sensor(sensor_api_key):
    return sensor.delete_sensor_by_api_key(sensor_api_key), 200