from django.urls import path
from . import views

urlpatterns = [
    path("",views.indexpage),
    path("sports/",views.sportspage,name="sports"),
    path("politics/",views.politicspage,name="politics"),
]
