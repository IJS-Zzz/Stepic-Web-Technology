from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# from django.db.models.manager import Manager


class QuestionManager(models.Manager):
    def new(self):
        # returns last added questions
        return super(QuestionManager, self).get_queryset().order_by('-added_at')
        # return supet(QuestionManager, self).get_queryset().order_by('-pk')

    def popular(self):
        # returns sorted questions on rating
        return super(QuestionManager, self).get_queryset().order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)  #, blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)  #, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text[:30]

    def __str__(self):
        return self.title[:30]