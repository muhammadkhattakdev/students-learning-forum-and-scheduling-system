from django.contrib import admin
from .models import * 


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    # Fields to edit in the admin detail view
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )

    # Fields to include when creating a new user via admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'birth_date', 'is_staff', 'is_active'),
        }),
    )

    # Search and ordering settings
    search_fields = ('email', 'username')
    ordering = ('email',)

# Register the model and admin class
admin.site.register(CustomUser, CustomUserAdmin)



# Register Teacher model
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
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

# Register Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
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
