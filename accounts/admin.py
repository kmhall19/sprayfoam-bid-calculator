from django.contrib import admin

# Register your models here.
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from companyprofile.models import CompanyProfile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ("company_name", "user")
