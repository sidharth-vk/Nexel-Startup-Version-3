from portfolio.models import projects
from blogs.models import BlogPost
from career.models import *
from service.models import *

def context_data(request):
    portfolio = projects.objects.all()
    allblogs = BlogPost.objects.all()[:3]
    category_instance = category.objects.get(title="Internship")
    allinternships = career.objects.filter(category=category_instance)
    internship_count = career.objects.filter(category=category_instance).count()
    training_count = Training.objects.all().count()
    allservices = service.objects.all()
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    else:
        profile = ""
    additional_data = {
        'portfolio': portfolio,
        'allblogs':allblogs,
        "allinternships":allinternships,
        "allservices":allservices,
        "profile":profile,
        "internship_count":internship_count,
        "training_count":training_count
    }
    return additional_data
