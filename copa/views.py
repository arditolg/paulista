from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(nome='Luis') 
    return render(request, 'copa/post_list.html', {'posts': posts})


