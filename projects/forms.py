from django import forms
from .models import Project, Measurements

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'client_name', 'location']

class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ['length', 'width', 'height', 'roof_pitch', 'insulation_type', 'thickness','roof_deck_width','peak_height','gable','eve_height',
                  'cc_wall_thickness','cc_roof_deck_thickness','cc_price_per_SBF','oc_wall_thickness','oc_roof_deck_thickness','oc_price_per_SBF','hy_wall_thickness','hy_roof_deck_thickness',
                  'hy_price_per_SBF','i1_name','i1_width','i1_height','i1_quantity','i2_name','i2_width','i2_height','i2_quantity','i3_name','i3_width','i3_height','i3_quantity']