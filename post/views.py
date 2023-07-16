from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def list_post(request):
    data = Post.objects.all()
    return render(request,'post_list.html', {'context': data})


def deatil_post(request, id_post):
    data = Post.objects.get(id = id_post)
    return render(request, 'deatil_post.html', {'context':data})    


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST ,request.FILES)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            post.save()
            return redirect ('/')
        
        return render(request, 'new_post.html', {'form':form}) 

    else:
        form = PostForm()   
        return render(request, 'new_post.html', {'form':form}) 
    

def edit_post(request, id_post):
  
    data = Post.objects.get(id=id_post)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
           
            return redirect ('/')  
        return render(request, 'new_post.html', {'form':form}) 
    else:
        form = PostForm(instance=data) 
        return render(request, 'edit_post.html', {'form':form}) 
    

# def new_post(request, id_post):
#     data = Post.objects.get(id=id_post)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             return render(request, 'new_post.html', {'form': form})
#     else:
#         form = PostForm(instance=data)
#         return render(request, 'new_post.html', {'form': form})