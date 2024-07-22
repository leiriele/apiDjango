from django.contrib import admin
from .models import User
# Lembre de criar um superUser:  python3 manage.py createsuperuser
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_nickname', 'user_name', 'user_email', 'user_age')
    search_fields = ('user_nickname', 'user_name', 'user_email')