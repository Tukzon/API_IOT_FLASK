import hashlib
import os
from services.db import get_db_connection

def hash(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def verify_hash(string, hash):
    return hash(string) == hash

def get_hash(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT password FROM admin WHERE username = ?""", (username,))
    password = cursor.fetchone()
    conn.close()
    return password[0]