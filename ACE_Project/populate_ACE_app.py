import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ACE_Project.settings')

import django
django.setup()

#Fake populate script
import random
from ACE_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # Create the new user entry
        user = User.objects.get_or_create(first=fake_first_name, last=fake_last_name, email=fake_email)[0]



if __name__ =='__main__':
    print("populating database!")
    populate(20)
    print("populating complete!")