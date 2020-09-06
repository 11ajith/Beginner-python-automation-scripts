# Generate random password 

import string
import random


def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(alphabet) for _ in range(length))

print(generate_password(8))