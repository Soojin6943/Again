from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from .models import FavoriteTag, FavoriteContent


class FavoriteTagInline(admin.TabularInline):
    model = FavoriteTag


class FavoriteContentInline(admin.TabularInline):
    model = FavoriteContent


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields": ("username", "password")}),
        ("개인정보", {"fields": ("first_name", "last_name", "email")}),
        ("추가필드", {"fields": ("profile_image", "short_description")}),
        ("권한", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("주요 일정", {"fields": ("last_login", "date_joined")}),
    ]
