# -*- coding:utf-8 -*-
# product_name: PyCharm
# project_name: mysite
# document_name: urls
# author: Lucifer
# create_time: 2019-03-10 21:45

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
