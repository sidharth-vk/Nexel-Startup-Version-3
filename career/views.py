from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def internship(request):
    categories = category.objects.get(title="Internship")
    data = career.objects.filter(category=categories)
    context={
        'data':data
    }
    return render(request,"career/internship.html",context)

def career_details(request,pk):
    data = career.objects.filter(slug=pk)
    instance = career.objects.get(slug=pk)
    skills = skill.objects.filter(career=instance)
    responsibility = responsibilities.objects.filter(career=instance)
    experiences = experience.objects.filter(career=instance)
    context={
        'data':data,
        "skills":skills,
        "responsibility":responsibility,
        "experiences":experiences
    }
    return render(request,"career/career_details.html",context)



def certificate_verify(request,pk):
    certificate = Certificate.objects.filter(certificate_id=pk)
    context = {
        "certificate":certificate
    }
    return render(request,"career/certificate_verify.html",context)




@csrf_exempt
def submit_internship(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        internship_for = request.POST.get('internship_for')
        college_name = request.POST.get('college_name')


        # Save data to the database
        application = InternshipApplication(
            name=name,
            email=email,
            phone=phone,
            internship_for=internship_for,
            college_name=college_name,
            convert=False
        )
        application.save()

        subject = 'Internship Registration Complete'
        from_email = 'nexel.cd@gmail.com'
        to_email = [email]
        html_content = render_to_string('mail/internship/registration.html', {'name': name,"email":email,"phone":phone,"internship_for":internship_for})

        # Create the email
        email = EmailMultiAlternatives(subject, '', from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()
        

        

        return JsonResponse({'status': 'success', 'message': 'Application submitted successfully'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'}, status=400)



def training(request):
    all_training = Training.objects.all()
    context = {
        "all_training":all_training
    }
    return render(request,'training/traning_page.html',context)

def training_details(request,pk):
    trainingdata = Training.objects.get(slug=pk)
    modules = Training_Modules.objects.filter(training=trainingdata)
    
    context = {
        "trainingdata":trainingdata,
        "modules":modules
    }
    return render(request,'training/details.html',context)

def download_task(request, task_id,week_no):
    task = get_object_or_404(Internship_task_week, internship=task_id,week_number=week_no)
    
    return redirect(task.link)