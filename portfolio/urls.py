from django.urls import path
from .views import *
urlpatterns = [
    path('',portfolio,name="portfolio"),
    path('<slug:pk>',portfolio_details,name="portfolio_details"),
]