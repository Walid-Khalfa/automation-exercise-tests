import random
import string
import time
from faker import Faker

fake = Faker()

def generate_random_email(prefix="test"):
    return f"{prefix}_{int(time.time())}_{random.randint(1000,9999)}@example.com"

def generate_random_user_data():
    return {
        "name": fake.name(),
        "email": generate_random_email("user"),
        "password": "Test1234!",
        "title": random.choice(["Mr", "Mrs"]),
        "day": str(random.randint(1, 28)),
        "month": fake.month_name(),
        "year": str(random.randint(1970, 2005)),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "United States",
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile": fake.phone_number(),
        "newsletter": True,
        "offers": True
    }
