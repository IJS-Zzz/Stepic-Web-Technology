from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db import models
from django.http import Http404
from django.urls import reverse



class QuestionManager(models.Manager):
    def new(self):
        # returns last added questions
        return self.order_by('-id')

    def popular(self):
        # returns sorted questions on rating
        return self.order_by('-rating')

    #FIXME
    def paginate(self, request, qs):
        try:
            limit = int(request.GET.get('limit', 10))
            if not 0 < limit <= 100:
                limit = 10
        except ValueError:
            limit = 10
        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            raise Http404

        # ! Paginator.baseurl !!!!!

        paginator = Paginator(qs, limit)
        try:
            page = paginator.page(page)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        return page

    # FIXME
    def main(self, since=None, limit=10):
        qs = self.order_by('-id')
        if since is not None:
            qs = qs.filter(id__lt=id)
        return qs[:1000]


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes", related_query_name="like", blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    # Need Test!
    def get_absolute_url(self):
        return reverse('qa:question', args=[str(self.id)])


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)  #, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text[:30]

    def __str__(self):
        return self.title[:30]