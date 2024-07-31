from faker import Faker

faker = Faker()


def generate_email_user():
    return faker.free_email()


def generate_user_pass():
    return faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)


def generate_user_name():
    return faker.name()
