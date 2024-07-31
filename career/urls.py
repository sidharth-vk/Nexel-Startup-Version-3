from django.urls import path
from .views import *
urlpatterns = [
    path('internship',internship,name="internship"),
    path('internship/<slug:pk>',career_details,name="career_internship_details"),
    path('certificate/verify/<pk>',certificate_verify,name="certificate_verify"),
    path('submit_internship/', submit_internship, name='submit_internship'),
    path('training/', training, name='training'),
    path('training/<slug:pk>', training_details, name='training_details'),
    path('task/download/<int:task_id>/<week_no>', download_task, name='download_task'),

]