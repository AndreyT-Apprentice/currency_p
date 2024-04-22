import string
import random
import csv

# from faker import Faker


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    password = ''

    for i in range(length):
        password += random.choice(chars)
    return password
