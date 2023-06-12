import hashlib
import random
import string
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

def string_a_lista(string):
    string = string.strip('[]')

    elementos = string.split(',')

    lista_enteros = [int(elemento) for elemento in elementos]

    return lista_enteros

def api_key_gen():
    letters = string.ascii_lowercase
    api_key = ''.join(random.choice(letters) for i in range(20))
    return api_key