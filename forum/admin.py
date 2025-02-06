from django.contrib import admin
from .models import *


# Register ForumModerator model
@admin.register(ForumModerator)
class ForumModeratorAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email')
    search_fields = ['user__email',]


    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['content',]
    readonly_fields = ('upvote_users', 'downvote_users')
    
