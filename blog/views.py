from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Post 
from django.utils import timezone

class PostListView(View):
    def get(self,request):
        posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request,'blog/post_list.html',{"posts":posts})
    
class PostDetailView(View):
    def get(self,request,id):
        post=get_object_or_404(Post,pk=id)
        return render(request,'blog/post_detail.html',{'post':post})
