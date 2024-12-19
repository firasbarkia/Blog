from django.shortcuts import render
from .models import Post
from django.utils.timezone import now

def post_list(request):
    return render(request, '/home/BarkiaFiras/barkiafiras.pythonanywhere.com/blog/post_list.html', {})
