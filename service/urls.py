from django.urls import path
from .views import *
urlpatterns = [
    path('',servicepage,name="servicepage"),
    path('<slug:pk>',service_details,name="service_details")
]