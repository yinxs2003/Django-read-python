from django.shortcuts import render

# Create your views here.
from blog.models import Post


def blog_index(request):
    post_list = Post.objects.order_by('-num_starts')[:5]
    return render(request, 'blog/post_index.html', {
        'post_list': post_list,
    })
