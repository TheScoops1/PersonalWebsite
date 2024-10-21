from django.urls import path

from . import views

app_name = 'personal'
urlpatterns =[
    path("", views.personal_website, name="personal"),
    path("pretty/", views.pretty_website, name='pretty')
]