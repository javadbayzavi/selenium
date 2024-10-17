import random
import string


def generate_random_email(domain="3t.io", length=10):
    letters = string.ascii_lowercase + string.digits

    random_string = 'selenium_' + ''.join(random.choices(letters, k=length))
    email = f"{random_string}@{domain}"
    return email


def generate_random_password(length=12):
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
