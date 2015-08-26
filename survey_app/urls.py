__author__ = 'kis'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<survey_id>\d+)/$', views.survey_detail, name='survey_detail'),
    url(r'/register', views.register, name='register')

]