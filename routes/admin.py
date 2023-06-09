from flask import Blueprint,jsonify, request

from controllers import company

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/api/v1/admin', methods=['POST'])
def create_admin():
    return company.new_admin(), 200