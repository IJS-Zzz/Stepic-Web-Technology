from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# from django.db.models.manager import Manager


class QuestionManager(models.Manager):
    def new(self):
        # returns last added questions
        # FIXME
        pass

    def popular(self):
        # returns sorted questions on rating
        # FIXME
        pass


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)  #, blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)  #, blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)