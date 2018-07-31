from django.conf.urls import url
from . import views
from . models import *

urlpatterns = [
    url(r'^add/textbook$', views.add_textbook, name='add_textbook'),
    url(r'^textbook/(?P<textbook_id>[0-9]+)/add_lesson$', views.add_lesson, name='add_lesson'),
    url(r'^textbook/(?P<textbook_id>[0-9]+)/$', views.textbook_detail, name='textbook_detail'),
    url(r'^textbook/(?P<textbook_id>[0-9]+)/lesson/(?P<lesson_id>[0-9]+)/$', views.lesson, name='lesson'),
    url(r'^textbook/(?P<textbook_id>[0-9]+)/lesson/(?P<lesson_id>[0-9]+)/delete/$', views.lesson_delete, name='lesson_delete'),
    url(r'^textbook/(?P<textbook_id>[0-9]+)/lesson/(?P<lesson_id>[0-9]+)/update/$', views.lesson_update, name='lesson_update'),
    url(r'^catalog$', views.TextbookListView.as_view(), name='catalog'),
]