from django import forms
from .models import Project, Measurements

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'client_name', 'location']

class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ['length', 'width', 'height', 'roof_pitch', 'insulation_type', 'thickness']
