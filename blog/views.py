from django.shortcuts import render
from .models import Post
from django.utils.timezone import now

def post_list(request):
    return render(request, 'blog/post_list.html', {})
