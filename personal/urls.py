from django.urls import path

from . import views

app_name = 'personal'
urlpatterns =[
    path("", views.personal_website, name="personal"),
    path("pretty/", views.pretty_website, name='pretty'),
    path("pretty/test", views.pretty_test_site, name="pretty_test"),
    path("personal_achievements", views.personal_achievments, name="personal_achievements")
]