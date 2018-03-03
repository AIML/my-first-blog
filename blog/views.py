from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(publish_time__lte=timezone.now()).order_by('publish_time')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})