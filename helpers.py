import random
import string

def generate_random_email():
    letters = string.ascii_lowercase
    local_part = ''.join(random.choice(letters) for _ in range(10))
    return f"{local_part}@test.ru"

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))