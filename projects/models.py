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
    # TESTING
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    roof_pitch = models.FloatField()
    insulation_type = models.CharField(max_length=50, choices=[
        ('open_cell', 'Open Cell'),
        ('closed_cell', 'Closed Cell')
    ])
    thickness = models.FloatField(default = 1)

    # ACTUAL
    roof_deck_width = models.FloatField(default = 1)
    peak_height = models.FloatField(default = 1)
    gable = models.FloatField(default = 1)
    eve_height = models.FloatField(default = 1)

    ## CLOSED CELL
    cc_wall_thickness = models.FloatField(default = 0)
    cc_roof_deck_thickness = models.FloatField(default = 0)
    cc_price_per_SBF = models.FloatField(default = 0)

    ## OPEN CELL
    oc_wall_thickness = models.FloatField(default = 0)
    oc_roof_deck_thickness = models.FloatField(default = 0)
    oc_price_per_SBF = models.FloatField(default = 0)

    ## HYBRID - OC + CC
    hy_wall_thickness = models.FloatField(default = 0)
    hy_roof_deck_thickness = models.FloatField(default = 0)
    hy_price_per_SBF = models.FloatField(default = 0)  

    ## DEDUCTIONS - Windows, Doors, Other
    i1_name = models.FloatField(default = 0)  
    i1_width = models.FloatField(default = 0)  
    i1_height = models.FloatField(default = 0)  
    i1_quantity = models.FloatField(default = 0)  

    i2_name = models.FloatField(default = 0)  
    i2_width = models.FloatField(default = 0)  
    i2_height = models.FloatField(default = 0)  
    i2_quantity = models.FloatField(default = 0)

    i3_name = models.FloatField(default = 0)  
    i3_width = models.FloatField(default = 0)  
    i3_height = models.FloatField(default = 0)  
    i3_quantity = models.FloatField(default = 0)

    def __str__(self):
        return f"Measurements for {self.project.name}"
