from django.shortcuts import render
from portfolio.models import *
from service.models import *
from .models import *
from blogs.models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from datetime import datetime
from django.core.mail import EmailMessage
# Create your views here.
def homepage(request):
    allservice = service.objects.all()
    project = projects.objects.all()[:2]
    project_feedback = ProjectFeedback.objects.all()
    blogs = BlogPost.objects.all()[:3]
    context = {
        'allservice':allservice,
        "project":project,
        'project_feedback':project_feedback,
        "blogs":blogs
    }
    return render(request,'index.html',context)


def about(request):
    teams = Team.objects.all()
    context = {
        "teams":teams
    }
    return render(request,"about.html",context)

def teampage(request):
    teams = Team.objects.all()
    context = {
        "teams":teams
    }
    return render(request,"team.html",context)


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)



def contact_us(request):
    return render(request,'contactus.html')


@csrf_exempt
def ajax_contact_us(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        company = request.POST.get('company')
        message = request.POST.get('message')

        # Basic validation
        if full_name and email and phone_number and company and message:
            contact_form = ContactForm(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                company=company,
                message=message
            )
            contact_form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'All fields are required'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})



def start_business(request):
    return render(request, 'start_your_buiness.html')


def submit_business(request):
    if request.method == 'POST':
        business_name = request.POST.get('business_name')
        business_description = request.POST.get('business_description')
        contact_email = request.POST.get('contact_email')
        business_goals = request.POST.get('business_goals')

        # Save to the database
        Business.objects.create(
            business_name=business_name,
            business_description=business_description,
            contact_email=contact_email,
            business_goals=business_goals
        )

        # Prepare email
        subject = 'Business Submission Confirmation'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = contact_email
        context = {
            'business_name': business_name,
            'business_description': business_description,
            'contact_email': contact_email,
            'business_goals': business_goals,
            'current_year': datetime.now().year,
        }

        message = render_to_string('mail/business_confirmation_email.html', context)
        email = EmailMessage(subject, message, from_email, [to_email])
        email.content_subtype = 'html'  # Use HTML content

        # Send email
        email.send(fail_silently=False)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
def submission_success(request):
    return render(request, 'submission_success.html')




def terms_and_conditions(request):
    data = Terms_and_condition.objects.first()
    context = {
        "data":data
    }
    return render(request,'community/terms_and_condition.html',context)

def privacy_policy(request):
    data = Privacy_policy.objects.first()
    context = {
        "data":data
    }
    return render(request,'community/privacy_policy.html',context)


def refund_policy(request):
    data = Refund_policy.objects.first()
    context = {
        "data":data
    }
    return render(request,'community/refund_policy.html',context)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscription.objects.filter(email=email).exists():
                return JsonResponse({"message": "Email already added."}, status=400)
            else:
                Subscription.objects.create(email=email)
                return JsonResponse({"message": "Subscription successful!", "redirect": "/"})
        else:
            return JsonResponse({"message": "Invalid email address."}, status=400)
    return JsonResponse({"message": "Invalid request method."}, status=405)