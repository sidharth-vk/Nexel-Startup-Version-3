from django.urls import path
from .views import *
urlpatterns = [
    path('',admin_home,name="admin_home"),
    path('internship',admin_all_internship,name="admin_all_internship"),
    path('internship/add-internship/', add_internship, name='add_internship'),
    path('edit_internship/<int:internship_id>/', edit_internship, name='edit_internship'),
    path('delete_internship/<int:internship_id>/', delete_internship, name='delete_internship'),
    path('internship/registration',admin_internship_all_registration,name="admin_internship_all_registration"),
    path('internship/all_intern',admin_internship_all_intern,name="admin_internship_all_intern"),
    path('internship/report_verify',admin_internship_all_report_verify,name="admin_internship_all_report_verify"),
    path('convert-to-intern/', convert_to_intern, name='convert-to-intern'),
    path('complete-report/<int:report_id>/', complete_report, name='complete_report'),
    
]