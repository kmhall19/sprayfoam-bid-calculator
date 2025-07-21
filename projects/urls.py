from django.urls import path
from .views import ProjectListView, ProjectCreateView, MeasurementsCreateView, QuoteCreateView, HomeDashboardView

urlpatterns = [
    path('', HomeDashboardView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/new/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/measurements/', MeasurementsCreateView.as_view(), name='add-measurements'),
    path('projects/new2/', QuoteCreateView.as_view(), name= 'quote-create')
]
