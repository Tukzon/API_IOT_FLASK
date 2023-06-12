from flask import Blueprint,jsonify, request

from controllers import admin

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/api/v1/admin', methods=['POST'])
def create_admin():
    return admin.new_admin(), 200