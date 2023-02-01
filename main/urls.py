from django.urls import path
from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home")
# path("index2/", views.index2, name="index2"),
]