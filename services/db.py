import sqlite3

# Path: services\db.py

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    #ADMIN
    cursor.execute("""CREATE TABLE IF NOT EXISTS admin(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )""")

    #COMPANY
    cursor.execute("""CREATE TABLE IF NOT EXISTS company(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        company_api_key TEXT
    )""")

    #LOCATION
    cursor.execute("""CREATE TABLE IF NOT EXISTS location(
        company_id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_name INTEGER NOT NULL,
        location_country TEXT NOT NULL,
        location_city TEXT NOT NULL,
        location_meta TEXT NOT NULL
    )""")

    #SENSOR
    cursor.execute("""CREATE TABLE IF NOT EXISTS sensor(
        location_id INTEGER NOT NULL,
        sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_name TEXT NOT NULL,
        sensor_category TEXT NOT NULL,
        sensor_meta TEXT NOT NULL,
        sensor_api_key TEXT NOT NULL
    )""")

    conn.commit()
    conn.close()
    return True
