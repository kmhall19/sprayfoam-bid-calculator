from django.urls import path
from .views import CostSettingsUpdateView

# In accounts/urls.py
urlpatterns = [
    path('settings/', CostSettingsUpdateView.as_view(), name='cost-settings'),
]