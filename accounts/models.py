from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class CostSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    material_cost_open_cell = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    material_cost_closed_cell = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    labor_cost_per_sqft = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    equipment_overhead = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    default_profit_margin = models.DecimalField(max_digits=5, decimal_places=2, default=20)

    def __str__(self):
        return f"Cost Settings for {self.user.username}"
