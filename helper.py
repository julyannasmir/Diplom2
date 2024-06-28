from faker import Faker
fake = Faker('ru_RU')


def generate_user_data():
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    return user_data

