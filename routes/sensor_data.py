from flask import Blueprint,jsonify, request

from controllers import sensor_data

sensor_data_bp = Blueprint('sensor_data_bp', __name__)

@sensor_data_bp.route('/api/v1/sensor_data', methods=['POST'])
def send_data():
    return sensor_data.create_data(), 201
    
@sensor_data_bp.route('/api/v1/sensor_data/<string:sensor_api_key>&from=<int:from_timestamp>&to=<int:to_timestamp>&sensor_id=<string:sensor_id>', methods=['GET'])
def get_data(sensor_api_key, from_timestamp, to_timestamp, sensor_id):
    return sensor_data.get_data(sensor_api_key, from_timestamp, to_timestamp, sensor_id), 200

@sensor_data_bp.route('/api/v1/sensor_data/<string:dev_password>', methods=['GET'])
def get_all_data(dev_password):
    return sensor_data.get_full_data(dev_password), 200