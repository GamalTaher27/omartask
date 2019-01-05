from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug  = models.SlugField()
    content =models.TextField(blank=True)
    created=models.DateTimeField(blank=True, default=datetime.datetime.now)
    active=models.BooleanField(default=True)
    tags=models.CharField(blank=True , max_length=100)
    def __str__(self):
        return self.title

# add new permissions
class Permissions(models.Model):
    permission_name = models.CharField(max_length=255, help_text="permission key")
    description = models.CharField(max_length=255, help_text="permission description")
    created_by = models.ForeignKey(User, db_index=True,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date when Role is added.")
    updated_on = models.DateTimeField(auto_now=True, help_text="Date when Role is modified.")
    enabled = models.BooleanField(default=True, help_text="Enable/Disable this object")

    def __str__(self):
        return self.permission_name

# create multiple group
class RoleGroup(models.Model):
    name = models.CharField(max_length=255, help_text="Short title of Role")
    created_by = models.ForeignKey(User, db_index=True,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date when Role is added.")
    updated_on = models.DateTimeField(auto_now=True, help_text="Date when Role is modified.")
    enabled = models.BooleanField(default=True, help_text="Enable/Disable this object")




# Assign Multiple group to user
class UserGroup(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name='role_group',on_delete=models.CASCADE)
    role_group = models.ForeignKey(RoleGroup, related_name='role_group_name', null = True, blank = True,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, db_index=True,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date when Role is added.")
    updated_on = models.DateTimeField(auto_now=True, help_text="Date when Role is modified.")
    enabled = models.BooleanField(default=True, help_text="Enable/Disable this object")


# add permisson to groups
class GroupPermissions(models.Model):
    role_group = models.ForeignKey(RoleGroup, related_name='role_permission_group_name',on_delete=models.CASCADE)
    permission_name = models.ForeignKey(Permissions,on_delete=models.CASCADE)


class Util :
 @staticmethod
 def has_permission(user, permission_name):
    role_group = UserGroup.objects.filter(user = user).values_list('role_group_id', flat = True)
    permission_names = GroupPermissions.objects.filter(role_group_id__in = role_group).values_list('permission_name', flat = True)
    if permission_name in permission_names:
        return True
    return False
