from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Measurements

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "date_created")
    search_fields = ("name", "client_name")

@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    list_display = ("project", "length", "width", "height", "roof_pitch", "insulation_type")
