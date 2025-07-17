from django.urls import path
from .views import QuoteDetailView

app_name = 'quotes'

urlpatterns = [
    path('<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
]
