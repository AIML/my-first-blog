from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(publish_time__lte=timezone.now()).order_by('publish_time')
    return render(request, 'blog/post_list.html',{'posts':posts})
