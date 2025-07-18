from django.contrib import admin
from accounts.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'id', 'email']


admin.site.register(User, UserAdmin)