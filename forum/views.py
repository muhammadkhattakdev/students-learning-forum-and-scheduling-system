from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages

@login_required(login_url='login')
def forum_home(request):
    posts = ForumPost.objects.all().order_by('-date_time')
    
    # Create paginator with 10 posts per page
    paginator = Paginator(posts, 1)
    
    # Get the current page number from the request
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    top_posts = ForumPost.objects.annotate(
        upvote_count=Count('upvote_users')
    ).order_by('-upvote_count')

    context = {
        'posts': page_posts,
        'top_posts': top_posts,
    }

    return render(request, 'forumPages/home.html', context)


@login_required
def create_forum_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        title = request.POST.get('post-title')

        if not content.strip():
            messages.error(request, "Post content cannot be empty.")
            return redirect('write_post_page')

        # Create the forum post
        ForumPost.objects.create(user=request.user, content=content, title=title)
        
        messages.success(request, "Your post has been successfully created!")
        return redirect('forum_homepage')  # Replace 'forum_home' with your desired page

    return render(request, 'forumPages/writeForumPost.html')


@login_required(login_url='login')
def read_forum_post(request):
    context = {}
    post_id = request.GET.get('post_id')
    print(post_id)
    top_posts = ForumPost.objects.annotate(
        upvote_count=Count('upvote_users')
    ).order_by('-upvote_count')
    context['top_posts'] = top_posts
    if post_id is not None:
        post_id = int(post_id)
        post = ForumPost.objects.get(id=post_id)
        related_replies = ForumPostReply.objects.filter(post=post)
        context['post'] = post
        context['related_replies'] = related_replies

    return render(request, 'forumPages/readPost.html', context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import ForumPost, ForumPostReply, CustomUser

class UpvotePostView(View):
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def post(self, request, post_id):
        post = get_object_or_404(ForumPost, id=post_id)
        user = request.user

        # Toggle upvote
        if user in post.upvote_users.all():
            post.upvote_users.remove(user)
            return JsonResponse({"message": "Upvote removed."}, status=200)
        else:
            post.upvote_users.add(user)
            post.downvote_users.remove(user)  # Remove any existing downvote
            return JsonResponse({"message": "Post upvoted."}, status=200)


class DownvotePostView(View):
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def post(self, request, post_id):
        post = get_object_or_404(ForumPost, id=post_id)
        user = request.user

        # Toggle downvote
        print("here")
        if user in post.downvote_users.all():
            post.downvote_users.remove(user)
            return JsonResponse({"message": "Downvote removed."}, status=200)
        else:
            print("here")
            post.downvote_users.add(user)
            post.upvote_users.remove(user)  # Remove any existing upvote
            return JsonResponse({"message": "Post downvoted."}, status=200)


class AddReplyView(View):
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def post(self, request, post_id):
        post = get_object_or_404(ForumPost, id=post_id)
        user = request.user

        try:
            data = json.loads(request.body)
            content = data.get("content")

            if not content:
                return JsonResponse({"error": "Reply content cannot be empty."}, status=400)

            reply = ForumPostReply.objects.create(user=user, post=post, content=content)
            return JsonResponse({"message": "Reply added successfully.", "reply_id": reply.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

