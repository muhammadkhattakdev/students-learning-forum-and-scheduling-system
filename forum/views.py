from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

@login_required(login_url='login')
def forum_home(request):
    context = {}

    return render(request, 'forumPages/home.html', context)



@login_required
def create_forum_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        
        if not content.strip():
            messages.error(request, "Post content cannot be empty.")
            return redirect('write_post_page')

        # Create the forum post
        ForumPost.objects.create(user=request.user, content=content)
        
        messages.success(request, "Your post has been successfully created!")
        return redirect('forum_home')  # Replace 'forum_home' with your desired page

    return render(request, 'forumPages/writeForumPost.html')