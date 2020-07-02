from django.urls import path
from .views import *

urlpatterns = [
    path('list/', people_list, name="people_list"),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>/', person_update, name="person_update"),
    path('delete/<int:id>/', person_delete, name="person_delete"),
]