from django.urls import path 
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_homepage'),
    path('write-post/', views.create_forum_post, name='write_post'),
    path('post/', views.read_forum_post, name='read_post'),
    path('api/upvote/<int:post_id>/', views.UpvotePostView.as_view(), name='upvote_post'),
    path('api/downvote/<int:post_id>/', views.DownvotePostView.as_view(), name='downvote_post'),
    path('api/reply/<int:post_id>/', views.AddReplyView.as_view(), name='add_reply'),
]

