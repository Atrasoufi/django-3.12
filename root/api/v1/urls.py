from django.urls import path
from .views import *

# app_name = "root"

urlpatterns = [
    path("test", test, name="test"),
    path("test2", test2, name="test2"),
    path("services", services, name="services"),
    path("categories", categories, name="categories"), 

]
