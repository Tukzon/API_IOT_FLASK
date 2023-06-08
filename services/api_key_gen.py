# Path: services/api_key_gen.py
import random
import string

def api_key_gen():
    letters = string.ascii_lowercase
    api_key = ''.join(random.choice(letters) for i in range(20))
    return api_key
