from django.urls import re_path
from LearnApp import views

#template tagging
app_name = 'LearnApp'

urlpatterns = [
    re_path(r'^first_page',views.first,name = 'first'),
    re_path(r'^relative',views.relative,name = 'relative'),
]
