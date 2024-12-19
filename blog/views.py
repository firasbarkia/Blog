from django.shortcuts import render
from .models import Post
from django.utils.timezone import now

def post_list(request):
    posts = Post.objects.filter(published_date__lte=now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
