from django.shortcuts import render
from .models import *
# Create your views here.
def portfolio_details(request,pk):
    details = projects.objects.filter(slug=pk)
    portfolio = projects.objects.all()[:3]
    context={
        "details":details,
        'portfolio':portfolio
    }
    return render(request,"portfolio/portfolio_details.html",context)

def portfolio(request):
    details = projects.objects.all()
    context={
        "details":details
    }
    return render(request,"portfolio/portfolio.html",context)

