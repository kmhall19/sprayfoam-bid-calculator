# accounts/forms.py
from django import forms
from .models import CostSettings

class CostSettingsForm(forms.ModelForm):
    class Meta:
        model = CostSettings
        fields = [
            'material_cost_open_cell',
            'material_cost_closed_cell',
            'labor_cost_per_sqft',
            'equipment_overhead',
            'default_profit_margin',
        ]
        widgets = {
            field: forms.NumberInput(attrs={'class': 'form-control'})
            for field in fields
        }
