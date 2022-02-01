from django.urls import re_path
from taskApp import views

urlpatterns=[

    re_path(r'^$', views.index),
    re_path(r'^show/$', views.show),
    re_path(r'^add/$', views.add),
    
    re_path(r'^book/$', views.bookApi),
    re_path(r'^book/([0-9]+)$', views.bookApi),

    re_path(r'^section/$', views.sectionApi),
    re_path(r'^section/([0-9]+)$', views.sectionApi)
]