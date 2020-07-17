import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Django.settings')

import django
django.setup()

# Fake POP script

import random
from firstApp.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(topName=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create a fake access record for the webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date= fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate()
    print("Populating complete!")
    