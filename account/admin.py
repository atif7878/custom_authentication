from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'email', 'full_name', 'date_of_birth', 'gender')

