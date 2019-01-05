from django.contrib import admin
from .models import Note,Permissions,RoleGroup,GroupPermissions,UserGroup
# Register your models here.

admin.site.register(Note)
admin.site.register(UserGroup)
admin.site.register(Permissions)
admin.site.register(RoleGroup)
admin.site.register(GroupPermissions)
