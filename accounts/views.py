from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# accounts/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from .models import CostSettings
from .forms import CostSettingsForm

class CostSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = CostSettings
    form_class = CostSettingsForm
    template_name = 'accounts/cost_settings_form.html'

    def get_object(self):
        obj, created = CostSettings.objects.get_or_create(user=self.request.user)
        return obj

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next') or '/'
