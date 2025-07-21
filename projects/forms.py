from django import forms
from .models import Project, Measurements

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'client_name', 'location','client_address_1','client_address_2','client_city','client_state','client_country','client_zip']

class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ['length', 'width', 'height', 'roof_pitch', 'insulation_type', 'thickness','roof_deck_width','peak_height','gable','eve_height',
                  'cc_wall_thickness','cc_roof_deck_thickness','cc_price_per_SBF','oc_wall_thickness','oc_roof_deck_thickness','oc_price_per_SBF','hy_wall_thickness','hy_roof_deck_thickness',
                  'hy_price_per_SBF','i1_name','i1_width','i1_height','i1_quantity','i2_name','i2_width','i2_height','i2_quantity','i3_name','i3_width','i3_height','i3_quantity']
        

# projects/forms.py
from django import forms
from .models import SprayFoamCalculation

class QuoteCalculationForm(forms.ModelForm):
    class Meta:
        model = SprayFoamCalculation
        fields = [
            # Example editable fields
            'cc_ext_house_walls_sqft', 'cc_wall_thickness', 'cc_house_roof_deck_sqft', 'cc_house_roof_deck_thickness',
            'oc_ext_house_walls_sqft', 'oc_wall_thickness', 'oc_house_roof_deck_sqft', 'oc_house_roof_deck_thickness',
            'hy_ext_house_walls_sqft', 'hy_wall_thickness', 'hy_house_roof_deck_sqft', 'hy_house_roof_deck_thickness',
            'cc_attic_floor_sqft', 'cc_attic_inches_thick',
            'fg_labor_sqft', 'fg_cost_sqft', 'fg_profit_sqft',
            'cd_labor_sqft', 'cd_cost_sqft', 'cd_profit_sqft',
            'bi_labor_sqft', 'bi_cost_sqft', 'bi_profit_sqft',
        ]

        