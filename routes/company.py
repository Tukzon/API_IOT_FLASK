from flask import Blueprint,jsonify, request

from controllers import company

company_bp = Blueprint('company_bp', __name__)

@company_bp.route('/api/v1/company', methods=['POST'])
def create_company():
    return company.new_company(), 200

@company_bp.route('/api/v1/company', methods=['GET'])
def get_companies():
    return company.get_company(), 200