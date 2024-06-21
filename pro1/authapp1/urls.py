from django.urls import path
from .views import *
urlpatterns=[
    path("suv/",suview),
    path("lgv/",lgview),
    path("lov/",loview)
]