import os
import sys
sys.path.append('/home/box/web/ask')


# !!!!!!!
# sys.path.append('/Users/smurov/Dropbox/web/Python/Stepic/stepic_project/Stepic-Web-Technology/ask')


os.environ['DJANGO_SETTINGS_MODULE'] = 'ask.settings'
import django
if hasattr(django, 'setup'):
    django.setup()

from django.contrib.auth.models import User
from django.db.models import Max
from django.utils import timezone

import time


def create_data_in_DB():
    from qa.models import Question
    from qa.models import Answer
    res = Question.objects.all().aggregate(Max('rating'))
    max_rating = res['rating__max'] or 0
    user, _ = User.objects.get_or_create(
        username='x',
        defaults={'password':'y', 'last_login': timezone.now()})
    for i in range(30):
        question = Question.objects.create(
            title='question ' + str(i),
            text='text ' + str(i),
            author=user,
            rating=max_rating+i
        )
    time.sleep(2)
    question = Question.objects.create(title='question last', text='text', author=user)
    question, _ = Question.objects.get_or_create(pk=3141592, title='question about pi', text='what is the last digit?', author=user)
    question.answer_set.all().delete()
    for i in range(10):
        answer = Answer.objects.create(text='answer ' + str(i), question=question, author=user)

if __name__ == "__main__":
    create_data_in_DB()