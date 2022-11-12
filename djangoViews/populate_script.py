import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoViews.settings')

import django
django.setup()

import random
from view.models import contact
from faker import Faker

fake = Faker()


def populate(value):
    for i in range(value):
        name = fake.name()
        address = fake.address()
        phone = random.randint(1,100)
        email = fake.email()
        obj = contact.objects.get_or_create(name=name, address=address, phone=phone, email=email)


def main():
    no = int(input('how many records do you want:'))
    populate(no)


if __name__ == '__main__':
    main()
