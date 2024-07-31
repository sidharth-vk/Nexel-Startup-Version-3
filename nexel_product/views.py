from django.shortcuts import render
from blogs.models import *
# Create your views here.

def drivemaster(request):
    blogs =  BlogPost.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request,'product/drivemaster/index.html',context)


def product_page(request):
    return render(request,'product/all_product.html')