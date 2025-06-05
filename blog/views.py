from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Post 
from django.utils import timezone
from .forms import PostForm

class PostListView(View):
    def get(self,request):
        posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request,'blog/post_list.html',{"posts":posts})
    
class PostDetailView(View):
    def get(self,request,id):
        post=get_object_or_404(Post,pk=id)
        return render(request,'blog/post_detail.html',{'post':post})

class PostNewView(View):
    def get(self,request):
        form=PostForm()
        return render(request,'blog/post_new.html',{'form':form})
    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect(post.get_absolute_url())
        return render(request,'blog/post_new.html',{'form':form})