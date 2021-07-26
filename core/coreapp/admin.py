from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import UserModel,MemberModel


class UserFilter(admin.ModelAdmin):
    list_filter = ('number', 'mail', 'tel_name','title','status','membercall',)
    list_display = ('firstname', 'lastname', 'number', 'mail', 'tel_name','title','status','membercall',)
    date_hierarchy = 'createdate'


class MemberFilter(admin.ModelAdmin):
    list_filter = ('username', 'workmail', 'position')
    list_display = ('firstname', 'lastname', 'username', 'workmail', 'position')




admin.site.site_header = 'Admin Panel'

admin.site.register(UserModel, UserFilter)
admin.site.register(MemberModel, MemberFilter)
admin.site.unregister(Group)
admin.site.unregister(User)
