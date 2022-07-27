from django.contrib import admin
from .models import Member, Entry, Share
from django.contrib.auth.admin import UserAdmin


class MemberConfig(UserAdmin):
    ordering = ('-id',)
    list_display = ('email', 'first_name', 'last_post', 'is_staff')


# class EntryConfig(UserAdmin):
#     list_display = ('entry__user_id', 'entry__entry_date',
#                     'entry__share_status')

# Register your models here.
admin.site.register(Member, MemberConfig)
admin.site.register(Entry)
admin.site.register(Share)
