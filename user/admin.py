from django.contrib import admin
from user.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'user_create_time']

admin.site.register(User, UserAdmin)