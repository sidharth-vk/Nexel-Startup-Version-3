from django.urls import path
from .views import *
urlpatterns = [
    path('',all_blogs,name="all_blogs"),
    path('<pk>',BlogDetails,name="BlogDetails")
]