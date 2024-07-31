from django.urls import path
from .views import *
urlpatterns = [
    path('login',login_view,name="login_view"),
      path('logout/', custom_logout_view, name='logout'),
      path('forget_password/', forget_password, name='forget_password'),
]
