from django.shortcuts import render
from .models import *
from home.models import *
# Create your views here.

def all_blogs(request):
    scrollbar = BlogPost.objects.all().order_by('?')[:3]
    all_blogs = BlogPost.objects.all()
    ads_image = ads_horizontal.objects.all().order_by('?')[:1]  
    category = Category.objects.all().order_by('?')[:10]  
    context = {
        "scrollbar": scrollbar,
        "all_blogs": all_blogs,
        "ads_image": ads_image,
        "category":category
    }
    return render(request, 'blogs/all_blogs.html', context)

def BlogDetails(request,pk):
    post = BlogPost.objects.get(slug=pk)
    posttag = BlogPostTag.objects.filter(post=post)
    # Assuming `post.content` is a long text field containing the blog content
    content = post.content
    content_parts = content.split('\n\n')  # Split into paragraphs based on double newline


    otherblogs = BlogPost.objects.all()
    if len(content_parts) > 2:
        first_part = '\n\n'.join(content_parts[:2])  # First two paragraphs
        second_part = '\n\n'.join(content_parts[2:])  # Remaining paragraphs after the second image

        context = {
            'post': post,
            'first_part': first_part,
            'second_part': second_part,
            'posttag':posttag,
            "blogs":otherblogs
        }
    else:
        context = {
            'post': post,
            'first_part': content,
            'second_part': None,  # No need to show a second part if less than two paragraphs
            'posttag':posttag,
            "blogs":otherblogs
        }

    return render(request,'blogs/blogdetails.html',context)