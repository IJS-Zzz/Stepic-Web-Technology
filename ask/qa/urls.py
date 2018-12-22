from django.conf.urls import url

from . import views

app_name = 'qa'

urlpatterns = [
    # url(r'^$', test),
    url(r'^$', views.new_questions, name='new'),
    url(r'^popular/$', views.popular_questions, name='popular'),
    url(r'^question/(?P<id>\d+)/$', views.question, name='question'),
]
