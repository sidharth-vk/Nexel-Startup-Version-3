from django.urls import path
from .views import *
urlpatterns = [
   path('profile',dash_home,name="dash_home"),
   path('all_internship',dash_all_internship,name="dash_all_internship"),
   path('all_internship/<pk>',dash_all_internship_details,name="dash_all_internship_details"),
   path('all_internship/report/<int:id>/<int:week>',internship_report_upload,name="internship_report_upload"),
   path('generate_certificate/<int:user_id>/<slug:internship_slug>/<int:assigned_id>/', generate_certificate_view, name='generate_certificate'),
   path('update-profile/', update_profile, name='update_profile'),
   path('update-password/', update_password, name='update_password'),
    path('request-email-update/', request_email_update, name='request_email_update'),
    path('verify-otp-and-update-email/', verify_otp_and_update_email, name='verify_otp_and_update_email'),
    path('dash_notification', dash_notification, name='dash_notification'),
    path('dash_resources', dash_resources, name='dash_resources'),
    path('dash_resources/<int:id>', dash_resources_data, name='dash_resources_data'),
    path('dash_resources/<int:id>/<int:pk>', resource_file_data, name='resource_file_data'),
    path('support/', support_page, name='support_page'),
    path('support_chat/', support_chat, name='support_chat'),
]
