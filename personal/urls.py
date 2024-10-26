from django.urls import path

from . import views

app_name = 'personal'
urlpatterns =[
    path("", views.home_page, name="home_page"),
    path("pretty/", views.pretty_website, name='pretty'),
    path("pretty/test", views.pretty_test_site, name="pretty_test"),
    path("personal_achievements", views.personal_achievments, name="personal_achievements")
]