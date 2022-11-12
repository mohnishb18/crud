import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoViews.settings')

import django
django.setup()

import random
from view.models import Employee
from faker import Faker

fake = Faker()


def populate(value):
    for i in range(value):
        eid = random.randint(1, 100)
        ename = fake.name()
        ecity = fake.city()
        esal = random.randint(15000, 60000)
        obj = Employee.objects.get_or_create(eid=eid, ename=ename, ecity=ecity, esal=esal)


def main():
    no = int(input('how many records do you want:'))
    populate(no)


if __name__ == '__main__':
    main()
