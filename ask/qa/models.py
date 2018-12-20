from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# from django.db.models.manager import Manager


class QuestionManager(models.Manager):
    def new(self):
        # метод возвращающий последние добавленные вопросы
        # FIXME
        pass

    def popular(self):
        # метод возвращающий вопросы отсортированные по рейтингу
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

"""
Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа

В качестве модели пользователя - используйте django.contrib.auth.models.User  из стандартной системы авторизации Django.

5) Рядом с моделью Question определите менеджер реализующий следующие методы

QuestionManager - менеджер модели Question
new - метод возвращающий последние добавленные вопросы
popular - метод возвращающий вопросы отсортированные по рейтингу
"""