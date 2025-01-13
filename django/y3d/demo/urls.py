from django.urls import path
from . import views

urlpatterns = [
    path('', views.greetings, name="greetings"),
    path('index', views.render_my_page, name="index"),
]
