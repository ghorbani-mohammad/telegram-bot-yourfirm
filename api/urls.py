from django.urls import re_path

from . import views

app_name = 'api'
urlpatterns = [
    re_path(r'^push_data', views.push_data, name='push_data'),
]
