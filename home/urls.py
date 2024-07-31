from django.urls import path
from .views import *
urlpatterns = [
    path('',homepage,name="homepage"),
    path('about',about,name="about"),
    path('meet-our-team',teampage,name="teampage"),
    path('contact_us',contact_us,name="contact_us"),
    path('subscribe/', subscribe, name='subscribe'),
    path('terms_and_conditions/', terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('refund_policy/', refund_policy, name='refund_policy'),
    path('ajax_contact_us/', ajax_contact_us, name='ajax_contact_us'),
    path('start-business/', start_business, name='start_business'),
    path('submit-business/', submit_business, name='submit_business'),
    path('submission-success/', submission_success, name='submission_success'),
]
