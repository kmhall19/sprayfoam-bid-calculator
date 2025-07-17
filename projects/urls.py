from django.urls import path
from .views import ProjectListView, ProjectCreateView, MeasurementsCreateView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('new/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/measurements/', MeasurementsCreateView.as_view(), name='add-measurements'),
]
