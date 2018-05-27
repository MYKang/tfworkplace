from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

UserAdmin.fieldsets += ('phone',)
UserAdmin.list_display += ('phone',)