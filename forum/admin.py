from django.contrib import admin
from .models import *


# Register ForumModerator model
@admin.register(ForumModerator)
class ForumModeratorAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_first_name', 'get_last_name', 'get_email')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_first_name', 'get_last_name')
    search_fields = ('user__first_name', 'user__last_name', 'content', 'user__email')
    readonly_fields = ('upvote_users', 'downvote_users')
    

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'