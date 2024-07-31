from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from career.models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
import random
import string
from .models import *
import joblib
import json
from django.views.decorators.http import require_POST
import openai
# Create your views here.



@login_required
def dash_home(request):
    return render(request,'career_dashboard/dash.html')

@login_required
def dash_all_internship(request):
    assigned_internship = Internship_Assigned.objects.filter(user=request.user,completed=False)
    certificate = Certificate.objects.filter(user=request.user)
    context = {
        "assigned_internship":assigned_internship,
        "certificate":certificate
    }
    return render(request,'career_dashboard/all_internship.html',context)

@login_required
def dash_all_internship_details(request,pk):
    internship_instance = career.objects.get(slug=pk)
    assigned_internship = Internship_Assigned.objects.filter(user=request.user,internship=internship_instance)
    assigned_internship_instance = Internship_Assigned.objects.get(user=request.user,internship=internship_instance)
    report = ProjectReport.objects.filter(internship_assigned=assigned_internship_instance)
    completed_count = ProjectReport.objects.filter(internship_assigned=assigned_internship_instance,submission="Completed").count()
    progress_percentage = (completed_count / int(assigned_internship_instance.internship.no_of_weeks)) * 100 if assigned_internship_instance.internship.no_of_weeks > 0 else 0
    reports = ProjectReport.objects.filter(internship_assigned=assigned_internship_instance).order_by('week_number')
    completed_weeks = set(report.week_number for report in reports if report.submission == "Completed")
    report_status = {report.week_number: report.submission for report in reports}

    certificate = Certificate.objects.filter(user=request.user,certificate_id=assigned_internship_instance.assigned_id)



    context = {
        "assigned_internship":assigned_internship,
        "report":report,
        "completed_count":completed_count,
        "progress_percentage":progress_percentage,
        'reports': reports,
        'completed_weeks': completed_weeks,
        'report_status': report_status,
        "certificate":certificate,
        "assigned_internship_instance":assigned_internship_instance
    }
    return render(request,'career_dashboard/internship_data_details.html',context)


def generate_certificate_view(request, user_id, internship_slug, assigned_id):
    try:
        user = get_object_or_404(User, id=user_id)
        internship = get_object_or_404(career, slug=internship_slug)

        assigned_internship = get_object_or_404(Internship_Assigned, id=assigned_id)
        assigned_internship.completed = True
        assigned_internship.save()
        
        certificate = Certificate.objects.create(
            user=user,
            name=user.get_full_name(),
            email=user.email,
            internship_for=internship,
            date_of_issue=timezone.now().date()
        )
        certificate.save()

        

        return JsonResponse({'status': 'success', 'message': 'Certificate generated successfully.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    


def internship_report_upload(request,id,week):
    assignedinternship = Internship_Assigned.objects.get(id=id)
    report_data = ProjectReport.objects.get(internship_assigned=id,week_number=week)
    if request.method == 'POST':
        report = request.POST.get('report')
        report_data.report = report
        report_data.save()  

        return redirect('dash_all_internship_details',assignedinternship.internship.slug)      
    context = {
        "report_data":report_data
    }
    return render(request,'career_dashboard/internship_report_upload.html',context)




@csrf_exempt
@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user_profile = get_object_or_404(Profile, user=request.user)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user_profile.mobileno = request.POST.get('mobile')
        user_profile.nationality = request.POST.get('nationality')
        user_profile.gender = request.POST.get('gender')

        if 'profile' in request.FILES:
            user_profile.profile = request.FILES['profile']
        user.save()
        user_profile.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)



@csrf_exempt
@login_required
def update_password(request):
    if request.method == 'POST':
        user = request.user
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not user.check_password(current_password):
            return JsonResponse({'status': 'error', 'message': 'Current password is incorrect'}, status=400)
        
        if new_password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'New passwords do not match'}, status=400)
        
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # Keeps the user logged in after password change

        return JsonResponse({'status': 'success', 'message': 'Password updated successfully'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



@login_required
@csrf_exempt
def request_email_update(request):
    if request.method == 'POST':
        new_email = request.POST.get('new_email')
        otp = ''.join(random.choices(string.digits, k=6))

        # Save the OTP and new email in the session
        request.session['otp'] = otp
        request.session['new_email'] = new_email

        # Send the OTP to the new email
        send_mail(
            'Email Verification Code',
            f'Your OTP for email verification is {otp}',
            'from@example.com',  # Replace with your email
            [new_email],
            fail_silently=False,
        )

        return JsonResponse({'status': 'success', 'message': 'OTP sent to the new email.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
@csrf_exempt
def verify_otp_and_update_email(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp == request.session.get('otp'):
            new_email = request.session.get('new_email')
            user = request.user
            user.email = new_email
            user.save()

            # Clear OTP and new email from session
            del request.session['otp']
            del request.session['new_email']

            return JsonResponse({'status': 'success', 'message': 'Email updated successfully.'})
        
        return JsonResponse({'status': 'error', 'message': 'Invalid OTP'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def dash_notification(request):
    return render(request,'career_dashboard/notification.html')


def dash_resources(request):
    resources = Resources.objects.all()
    context = {
        "resources":resources
    }
    return render(request,'career_dashboard/resources.html',context)

def resource_file_data(request,id,pk):
    resources = Resources_file_data.objects.get(id=pk)
    context = {
        "resources":resources
    }
    return render(request,'career_dashboard/resource_file_data.html',context)

def dash_resources_data(request,id):
    resources_file = Resources_file_data.objects.filter(resources=id)
    resources_video = Resources_video_data.objects.filter(resources=id)
    resources_folder = Resources_Folder_data.objects.filter(resources=id)
    context = {
        "resources_file":resources_file,
        "resources_video":resources_video,
        "resources_folder":resources_folder,
        "id":id
    }
    return render(request,'career_dashboard/dash_resources_data.html',context)



def support_page(request):
    return render(request,'career_dashboard/support.html')



@csrf_exempt
def support_chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').strip().lower()
        
        # Define responses for different queries
        responses = {
    'hello': 'Hi there! How can I assist you with your internship today?',
    'hi': 'Hello! What can I help you with regarding your internship?',
    'what is your name': 'I am your support assistant for internship-related queries. How can I help you?',
    'who are you': 'I am here to assist with any questions you have about your internship. How can I assist you today?',
    'how can i contact support': 'You can reach out to our support team by emailing support@example.com.',
    'contact support': 'For support, please email us at support@example.com.',
    'hours of operation': 'Our support team is available 24/7 to assist with your internship queries.',
    'when are you available': 'We are available around the clock for any internship-related assistance.',
    'refund policy': 'For information about our refund policy, please refer to the "Refunds" section on our website.',
    'how do i get a refund': 'To request a refund, visit the "Refunds" section on our website or contact our support team.',
    'shipping policy': 'You can view our shipping policy under the "Shipping" section on our website.',
    'delivery time': 'Delivery times vary. Check our shipping page for details on delivery times.',
    'track my order': 'To track your order, visit the "Order Tracking" section on our website.',
    'update my order': 'To update your order, please contact support@example.com as soon as possible.',
    'cancel my order': 'To cancel your order, contact our support team immediately.',
    'password reset': 'To reset your password, use the "Forgot Password" link on the login page.',
    'login issues': 'If you’re having login issues, try resetting your password or contact support for assistance.',
    'account settings': 'Manage your account settings by logging into your account on our website.',
    'change email': 'To change your email address, go to the "Account Settings" page on our website.',
    'update profile': 'To update your profile, log in to your account and visit the "Profile" section.',
    'privacy policy': 'Read our privacy policy under the "Privacy" section on our website.',
    'terms and conditions': 'Our terms and conditions can be found in the "Terms" section on our website.',
    'how to use the app': 'Find usage instructions in the "Help" section of the app or on our website.',
    'report a bug': 'To report a bug, email us with details at support@example.com.',
    'feedback': 'We welcome feedback! Send your comments to feedback@example.com.',
    'feature request': 'For feature requests, contact support@example.com with your suggestions.',
    'technical support': 'For technical support, reach out to us at support@example.com.',
    'general inquiry': 'For general inquiries, email us at info@example.com.',
    'internship details': 'For details about your internship, please check the internship portal or contact your internship coordinator.',
    'internship certificate': 'Internship certificates are typically issued upon completion of the internship. For specific timelines, please contact your coordinator.',
    'when will the internship start': 'The start date for internships can be found on the internship portal or you can contact your coordinator for exact dates.',
    'how to change email': 'To change your email address, log in to your account and update your email in the "Account Settings" section.',
    'how to change name': 'To update your name, please contact your internship coordinator or support team for assistance.',
    'how to apply for an extension': 'To apply for an extension, please submit a request through the internship portal or contact your coordinator.',
    'where to submit reports': 'Submit your internship reports through the internship portal or as instructed by your coordinator.',
    'how to request a reference letter': 'Request a reference letter from your supervisor or coordinator through email or the internship portal.',
    'default': 'I\'m sorry, I didn\'t understand your question. Could you please provide more details or rephrase your question?'
}

        # Determine the response
        reply = responses.get(user_message, responses['default'])
        
        return JsonResponse({'reply': reply})
    
    return JsonResponse({'reply': 'Invalid request method.'}, status=400)

