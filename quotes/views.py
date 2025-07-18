from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Quote
from projects.models import Project

class QuoteDetailView(LoginRequiredMixin, DetailView):
    model = Quote
    template_name = 'quotes/quote_detail.html'
    context_object_name = 'quote'

    def get_object(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'], user=self.request.user)
        return get_object_or_404(Quote, project=project)
