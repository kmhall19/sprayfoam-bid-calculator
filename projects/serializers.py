from rest_framework import serializers
from .models import Project, Measurements

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "client_name", "location", "date_created", "measurements"]
