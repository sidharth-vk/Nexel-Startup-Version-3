from django.shortcuts import render , get_object_or_404, redirect
from .decorators import superuser_required
from career.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import secrets
import string
from django.db.models import Q

# Create your views here.

@superuser_required
def admin_home(request):
    total_internship = career.objects.all().count()
    total_application = InternshipApplication.objects.all().count()
    total_interns = Internship_Assigned.objects.all().count()
    total_report = ProjectReport.objects.all().count()
    total_revenue = ProjectReport.objects.all().count() * 299
    total_courses = Training.objects.all().count()

    context = {
        "total_internship":total_internship,
        "total_application":total_application,
        "total_interns":total_interns,
        "total_report":total_report,
        "total_revenue":total_revenue,
        "total_courses":total_courses
    }
    return render(request,'admin_templates/index.html',context)



@superuser_required
def admin_internship_all_registration(request):
    all_leads = InternshipApplication.objects.filter(convert=False).order_by('-id')
    context = {
        "all_leads":all_leads
    }
    return render(request,'admin_templates/internships/all_registration.html',context)



@csrf_exempt
@superuser_required
@require_POST
def convert_to_intern(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    internship_for = request.POST.get('internship_for')
    college_name = request.POST.get('college_name')

    Internship_application = InternshipApplication.objects.get(id=id)
    Internship_application.convert = True
    Internship_application.save()


    
    # Check if the user already exists
    username = email.split('@')[0]
    user, created = User.objects.get_or_create(username=username, email=email)
    if created:
        
        alphabet = string.ascii_letters + string.digits
        random_password = ''.join(secrets.choice(alphabet) for i in range(12))
        user.set_password(random_password)  # Set a default unusable password
        user.save()
        profile = Profile.objects.create(user=user,mobileno=phone)
        profile.save()

    # Send email with username and password
        subject = 'Welcome to Your Internship at Nexel! 🎉'

        message = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333333;
                    padding: 20px;
                }}
                .container {{
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                    margin: 0 auto;
                }}
                h1 {{
                    color: #4CAF50;
                }}
                p {{
                    line-height: 1.6;
                }}
                .button {{
                    display: inline-block;
                    padding: 10px 20px;
                    font-size: 16px;
                    color: #ffffff;
                    background-color: #4CAF50;
                    text-decoration: none;
                    border-radius: 5px;
                }}
                .footer {{
                    margin-top: 20px;
                    font-size: 12px;
                    color: #777777;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello {username},</h1>
                <p>Welcome to Nexel! We're thrilled to have you on board as our new intern.</p>
                <p>Your account has been created successfully. Here are your login details:</p>
                <ul>
                    <li><strong>Username:</strong> {username}</li>
                    <li><strong>Password:</strong> {random_password}</li>
                </ul>
                <p>For your security, please login and change your password immediately after your first login.</p>
                <p>If you have any questions or need assistance, feel free to reach out to our support team.</p>
                <p>Best regards,<br>The Nexel Team</p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Nexel. All rights reserved.</p>
            </div>
        </body>
        </html>
        """

        send_mail(subject, message, settings.EMAIL_HOST_USER, [email], html_message=message)



    # Find the internship application
    application = InternshipApplication.objects.filter(email=email).first()

    if not application:
        return JsonResponse({'error': 'Application not found'}, status=404)

    # Find the career
    career_instance = career.objects.filter(title=internship_for).first() 

    if not career_instance:
        return JsonResponse({'error': 'Career not found'}, status=404)

    # Create Offerletter
    offer_letter = Offerletter.objects.create(
        name=name,
        email=email,
        internship_for=career_instance
    )
    offer_letter.save

    # Create Internship_Assigned
    internship_assigned = Internship_Assigned.objects.create(
        user=user,
        internship=career_instance,
        offer_letter=offer_letter,
    )

    return JsonResponse({'success': 'Internship assigned successfully'})



@superuser_required
def admin_internship_all_intern(request):
    all_leads = Internship_Assigned.objects.all().order_by('completed')
    context = {
        "all_leads":all_leads
    }
    return render(request,'admin_templates/internships/all_interns.html',context)





@superuser_required
def admin_internship_all_report_verify(request):
    all_leads = ProjectReport.objects.filter( (Q(submission="Pending") | Q(submission="Rewrite") | Q(submission="Rejected")) & ~Q(report="") ).order_by('-id')
    context = {
        "all_leads":all_leads
    }
    return render(request,'admin_templates/internships/all_report_verify.html',context)



@superuser_required
def complete_report(request, report_id):
    # Fetch the report object
    report = get_object_or_404(ProjectReport, id=report_id)
    # Update the submission status to 'Completed'
    report.submission = 'Completed'
    report.save()
    # Redirect back to the previous page or to a specific URL
    return redirect('admin_internship_all_report_verify')  # replace 'desired-view-name' with your target view name





@superuser_required
def admin_all_internship(request):
    allinternship = career.objects.all()
    context = {
        "allinternship":allinternship
    }
    return render(request,'admin_templates/internships/all_internships.html',context)


def add_internship(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        shortdes = request.POST.get('shortdes')
        img = request.FILES.get('img')
        category_id = request.POST.get('category')
        edu = request.POST.get('edu')
        des = request.POST.get('des')
        mode = request.POST.get('mode')
        startdate = request.POST.get('startdate')
        duration = request.POST.get('duration')
        no_of_weeks = int(request.POST.get('no_of_weeks'))
        stipend = request.POST.get('stipend')
        code = request.POST.get('code')
        slug = request.POST.get('slug')

        selected_category = category.objects.get(id=category_id)
        new_career = career(
            title=title,
            shortdes=shortdes,
            img=img,
            category=selected_category,
            edu=edu,
            des=des,
            mode=mode,
            startdate=startdate,
            duration=duration,
            no_of_weeks=no_of_weeks,
            stipend=stipend,
            code=code,
            slug=slug
        )
        new_career.save()

        # Save skills
        skill_names = request.POST.getlist('skill_name')
        skill_descriptions = request.POST.getlist('skill_des')
        for name, description in zip(skill_names, skill_descriptions):
            if name and description:
                new_skill = skill(career=new_career, name=name, des=description)
                new_skill.save()

        # Save responsibilities
        responsibility_names = request.POST.getlist('responsibility_name')
        responsibility_descriptions = request.POST.getlist('responsibility_des')
        for name, description in zip(responsibility_names, responsibility_descriptions):
            if name and description:
                new_responsibility = responsibilities(career=new_career, name=name, des=description)
                new_responsibility.save()

        # Save experiences
        experience_names = request.POST.getlist('experience_name')
        experience_descriptions = request.POST.getlist('experience_des')
        for name, description in zip(experience_names, experience_descriptions):
            if name and description:
                new_experience = experience(career=new_career, name=name, des=description)
                new_experience.save()

        # Save Internship_task_week
        for i in range(1, no_of_weeks + 1):
            week_number = request.POST.get(f'week_number_{i}')
            week_link = request.POST.get(f'week_link_{i}')
            if week_number and week_link:
                new_task_week = Internship_task_week(internship=new_career, week_number=week_number, link=week_link)
                new_task_week.save()

        return redirect('admin_all_internship')  # Redirect to a success page or the appropriate URL

    categories = category.objects.all()
    return render(request, 'admin_templates/internships/add_internship.html', {'categories': categories})




def edit_internship(request, internship_id):
    internship = get_object_or_404(career, id=internship_id)
    
    if request.method == 'POST':
        internship.title = request.POST.get('title')
        internship.shortdes = request.POST.get('shortdes')
        internship.img = request.FILES.get('img') if request.FILES.get('img') else internship.img
        category_id = request.POST.get('category')
        internship.category = category.objects.get(id=category_id)
        internship.edu = request.POST.get('edu')
        internship.des = request.POST.get('des')
        internship.mode = request.POST.get('mode')
        internship.startdate = request.POST.get('startdate')
        internship.duration = request.POST.get('duration')
        internship.no_of_weeks = int(request.POST.get('no_of_weeks'))
        internship.stipend = request.POST.get('stipend')
        internship.code = request.POST.get('code')
        internship.slug = request.POST.get('slug')

        internship.save()

        # Update skills
        internship.skill_set.all().delete()  # Clear existing skills
        skill_names = request.POST.getlist('skill_name')
        skill_descriptions = request.POST.getlist('skill_des')
        for name, description in zip(skill_names, skill_descriptions):
            if name and description:
                new_skill = skill(career=internship, name=name, des=description)
                new_skill.save()

        # Update responsibilities
        internship.responsibilities_set.all().delete()  # Clear existing responsibilities
        responsibility_names = request.POST.getlist('responsibility_name')
        responsibility_descriptions = request.POST.getlist('responsibility_des')
        for name, description in zip(responsibility_names, responsibility_descriptions):
            if name and description:
                new_responsibility = responsibilities(career=internship, name=name, des=description)
                new_responsibility.save()

        # Update experiences
        internship.experience_set.all().delete()  # Clear existing experiences
        experience_names = request.POST.getlist('experience_name')
        experience_descriptions = request.POST.getlist('experience_des')
        for name, description in zip(experience_names, experience_descriptions):
            if name and description:
                new_experience = experience(career=internship, name=name, des=description)
                new_experience.save()

        # Update Internship_task_week
        internship.internship_task_week_set.all().delete()  # Clear existing weeks
        for i in range(1, internship.no_of_weeks + 1):
            week_number = request.POST.get(f'week_number_{i}')
            week_link = request.POST.get(f'week_link_{i}')
            if week_number and week_link:
                new_task_week = Internship_task_week(internship=internship, week_number=week_number, link=week_link)
                new_task_week.save()

        return redirect('admin_all_internship')  # Redirect to a success page or the appropriate URL

    categories = category.objects.all()
    context = {
        'internship': internship,
        'categories': categories,
        'skills': internship.skill_set.all(),
        'responsibilities': internship.responsibilities_set.all(),
        'experiences': internship.experience_set.all(),
        'task_weeks': internship.internship_task_week_set.all()
    }
    return render(request, 'admin_templates/internships/edit_internship.html', context)



def delete_internship(request, internship_id):
    internship = get_object_or_404(career, id=internship_id)
    internship.delete()
    return redirect('admin_all_internship')