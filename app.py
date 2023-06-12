from flask import Flask
from services.db import create_tables
from routes import location, sensor, company, admin, sensor_data

app = Flask(__name__)

app.register_blueprint(location.location_bp)
app.register_blueprint(sensor.sensor_bp)
app.register_blueprint(company.company_bp)
app.register_blueprint(admin.admin_bp)
app.register_blueprint(sensor_data.sensor_data_bp)

if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=True)

