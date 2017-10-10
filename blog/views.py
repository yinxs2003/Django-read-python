
from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import stringfilter

from blog.models import Post, About


def blog_index(request):
    post_list = Post.objects.order_by('-num_starts')[:5]
    return render(request, 'blog/index.html', {
        'post_list': post_list,
    })


def about(request):
    return render(request, 'blog/about.html', {'about_list': About.objects.all()})
