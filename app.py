from flask import Flask, request, jsonify
from services.db import get_db_connection
import sqlite3

app = Flask(__name__)

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    #ADMIN
    cursor.execute("""CREATE TABLE IF NOT EXISTS admin(
        Username TEXT PRIMARY KEY,
        Password TEXT NOT NULL
    )""")

    #COMPANY
    cursor.execute("""CREATE TABLE IF NOT EXISTS company(
        CompanyID INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        company_api_key TEXT
    )""")

    #LOCATION
    cursor.execute("""CREATE TABLE IF NOT EXISTS location(
        location_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_id INTEGER NOT NULL,
        sensor_name TEXT NOT NULL,
        sensor_category TEXT NOT NULL,
        sensor_meta TEXT NOT NULL,
        sensor_api_key TEXT NOT NULL
    )""")

    conn.commit()
    conn.close()

create_tables()
