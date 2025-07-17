from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Measurements(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    roof_pitch = models.FloatField()
    insulation_type = models.CharField(max_length=50, choices=[
        ('open_cell', 'Open Cell'),
        ('closed_cell', 'Closed Cell')
    ])
    thickness = models.FloatField()

    def __str__(self):
        return f"Measurements for {self.project.name}"
