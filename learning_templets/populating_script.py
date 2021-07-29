import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_templets.settings')

import django
django.setup()

import random
from basic_app.models import Question,Choice
from faker import Faker

fakegen = Faker()
Question_list = ['what\'s your name?', 'What\'s your e-mail adress?','where do u live?']

def choice_mix (number):
    if number == 0:
        var1 = fakegen.name()
    elif number ==1:
        var1 = fakegen.address()
    elif number ==2:
        var1 = fakegen.currency()
    return var1

def populate(N=3):
    for i in range(3):
        t = Question.objects.get_or_create(question_text=Question_list[i], pub_date = fakegen.date())[0]
        for entry in range(N):
                t.choice_set.get_or_create(choice_text=choice_mix(i),votes=random.randint(5,100))[0]

    # t=Question.objects.get_or_create(question_text=Question_list[0], pub_date = fakegen.date())[0]
    # t.save()
    # for entry in range(N):
    #     t.choice_set.get_or_create(choice_text=fakegen.name(),votes=random.randint(5,100))[0]
    #
    # t=Question.objects.get_or_create(question_text=Question_list[1], pub_date = fakegen.date())[0]
    # t.save()
    # for entry in range(N):
    #     t.choice_set.get_or_create(choice_text=fakegen.address(),votes=random.randint(5,100))[0]
    #
    # t=Question.objects.get_or_create(question_text=Question_list[2], pub_date = fakegen.date())[0]
    # t.save()
    # for entry in range(N):
    #     t.choice_set.get_or_create(choice_text=fakegen.currency(),votes=random.randint(5,100))[0]

if __name__ == '__main__':
    print('populating script....')
    populate(2)
    print('POPULATING COMPLETE!')
