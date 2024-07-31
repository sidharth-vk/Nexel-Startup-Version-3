from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_mail_certificate(name,internship_for,date_of_issue,certificate_image,email):
    name = name
    url = f"http://www.nexel.in/{certificate_image}" 
    emailcontext ={
                    'user':name,
                    "internship_for":internship_for,
                    "date_of_issue":date_of_issue,
                    "url":url
                }

    html_message = render_to_string('mail/internship/certificate_mail.html', emailcontext)
    send_mail("⭐ Congratulations / Nexel Internship Completion certification",
                '',
                'nexel.cd@gmail.com',
                [email],
                html_message=html_message,
                fail_silently=False,
                )