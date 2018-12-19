from django.conf.urls import url
from views import test

urlpatterns = [
    url(r'^(?P<num>\d+)/$', test),
]
