from django.conf.urls import url

from views import test


app_name = 'qa'

urlpatterns = [
    # url(r'^$', test),
    url(r'^(?P<num>\d+)/$', test),
]
