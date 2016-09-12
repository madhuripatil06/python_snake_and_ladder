from django.conf.urls import url
from views.manager import *

urlpatterns = [
    url(r'^login/$', Manager.as_view()),
]
