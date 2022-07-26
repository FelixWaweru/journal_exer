from django.contrib import admin
from .models import Member, Entry, Share
from django.contrib.auth.admin import UserAdmin


class MemberConfig(UserAdmin):
    ordering = ('-id',)
    list_display = ('email', 'first_name', 'is_active', 'is_staff')


# Register your models here.
admin.site.register(Member, MemberConfig)
admin.site.register(Entry)
admin.site.register(Share)
