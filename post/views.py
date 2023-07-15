from django.shortcuts import render
from .models import Post
# Create your views here.

def list_post(request):
    data = Post.objects.all()
    return render(request,'post_list.html', {'context': data})