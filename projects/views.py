from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project, Measurements
from quotes.models import Quote
from .forms import ProjectForm, MeasurementsForm
from quotes.utils import calculate_quote_for_project

# 1. List all projects
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user).order_by('-date_created')

# 2. Create a new project
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return redirect('add-measurements', pk=self.object.pk)

# 3. Add measurements
class MeasurementsCreateView(LoginRequiredMixin, CreateView):
    model = Measurements
    form_class = MeasurementsForm
    template_name = 'projects/measurements_form.html'

    def dispatch(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'], user=request.user)
        if hasattr(project, 'measurements'):
            # If measurements already exist, redirect to quote view
            return redirect('quote-detail', pk=project.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'], user=self.request.user)
        form.instance.project = project
        form.save()

        # Trigger quote calculation
        calculate_quote_for_project(project)

        return redirect('quotes:quote-detail', pk=project.pk)
    
# 4. View quote summary
class QuoteDetailView(LoginRequiredMixin, DetailView):
    model = Quote
    template_name = 'quotes/quote_detail.html'
    context_object_name = 'quote'

    def get_object(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'], user=self.request.user)
        return get_object_or_404(Quote, project=project)
