import os
from pydoc import describe
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
import django
django.setup()

import random
from faker import Faker
from faker_vehicle import VehicleProvider

from product.models import Product

fake = Faker()
fake.add_provider(VehicleProvider)

def populate(n):
    for _ in range(n):
        f_name = fake.vehicle_year_make_model() # 2014 Volkswagen Golf
        f_description = fake.vehicle_category() # Wagon
        f_quantity = random.randrange(50, 150)
        f_price = random.randrange(30000, 150000)
        f_is_available = bool(random.getrandbits(1))
        Product.objects.get_or_create(
            name= f_name,
            description= f_description,
            quantity= f_quantity,
            price= f_price,
            is_available = f_is_available
            )[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(15) # number of faker data
    print('Populating Complete!')


