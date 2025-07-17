from django.db import models

# Create your models here.
from django.db import models
from projects.models import Project
from django.contrib.auth.models import User

class Quote(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    spray_area = models.FloatField()
    material_cost = models.DecimalField(max_digits=10, decimal_places=2)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    equipment_cost = models.DecimalField(max_digits=10, decimal_places=2)
    overhead_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)
    profit_margin = models.DecimalField(max_digits=5, decimal_places=2)
    final_bid = models.DecimalField(max_digits=12, decimal_places=2)
    date_generated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote for {self.project.name}"
