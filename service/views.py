from django.shortcuts import render,redirect

from portfolio.models import projects
from .models import *
# Create your views here.
def servicepage(request):
    allservice = service.objects.all()
    context = {
        "allservice":allservice
    }
    return render(request,"service/service.html",context)


def service_details(request,pk):
    service_detail = service.objects.filter(slug=pk)
    if service_detail:

        service_detail_instance = service.objects.get(slug=pk)
        service_benefit = service_benefits.objects.filter(service=service_detail_instance)
        service_works = service_work.objects.filter(service=service_detail_instance)
        solutions = solution.objects.filter(service=service_detail_instance) 

        portfolio = projects.objects.all()[:3]
        
        context = {
            'servide_detail':service_detail,
            "service_benefit":service_benefit,
            "service_works":service_works,
            "solutions":solutions,
            'portfolio':portfolio
        }
        return render(request,'service/service_details.html',context)
    else:
        return redirect('/')