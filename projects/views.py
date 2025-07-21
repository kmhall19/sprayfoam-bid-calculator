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
from projects.utils import generate_readonly_fields_html 

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

        return redirect('quote-detail', pk=project.pk)
    
# 4. View quote summary
class QuoteDetailView(LoginRequiredMixin, DetailView):
    model = Quote
    template_name = 'quotes/quote_detail.html'
    context_object_name = 'quote'

    def get_object(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'], user=self.request.user)
        return get_object_or_404(Quote, project=project)


from collections import defaultdict
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import SprayFoamCalculation
from accounts.models import CostSettings
from .forms import QuoteCalculationForm

# Constants
PPU = {'oc': 0.34, 'cc': 1.80, 'hy': 2.65}  # Price per board foot
SET_COST = 1625  # Cost per spray foam set
BF_PER_SET = 15000  # Board feet per set
COMMISSION_RATE = 0.10  # 10% commission

class QuoteCreateView(CreateView):
    model = SprayFoamCalculation
    #form_class = QuoteCalculationForm
    template_name = "projects/quote_form.html"
    success_url = reverse_lazy("quote-calculator")
    #fields = '__all__'
    def get_initial(self):
        initial = super().get_initial()
        try:
            cost_settings = CostSettings.objects.latest('id')
            # Example: Set cost per set from settings
            initial.update({
                'ppu_cc': cost_settings.cc_ppu,
                'ppu_oc': cost_settings.oc_ppu,
                'ppu_hy': cost_settings.hy_ppu,
                #'set_cost': cost_settings.,
                'commission_rate': cost_settings.def_comm_rate,
                'fg_labor_sqft':cost_settings.fg_labor_per_sqft,
                'bi_labor_sqft':cost_settings.bi_lb_brd_foot,
                'cd_labor_sqft':cost_settings.cd_labor_per_sqft
                # Add other defaults here
            })
        except CostSettings.DoesNotExist:
            pass
        return initial
    fields = [
            # Closed Cell
            'cc_ext_house_walls_sqft', 'cc_wall_thickness',
            'cc_house_roof_deck_sqft', 'cc_house_roof_deck_thickness',
            'cc_house_roof_deck_vol', 'cc_house_total_sbf',
            'cc_sound_batts', 'cc_garage_walls', 'cc_garage_roof_deck',
            'cc_garage_total_sbf', 'cc_sets', 'cc_mtr_cost',
            'cc_man_hours', 'cc_shifts', 'cc_incedentals',
            'cc_sprayer_cost', 'cc_labor_cost', 'cc_total_cost',
            'cc_total_price', 'cc_profit', 'cc_margins',
            'cc_commission', 'cc_profit_after_com',

            # Open Cell
            'oc_ext_house_walls_sqft', 'oc_wall_thickness',
            'oc_house_roof_deck_sqft', 'oc_house_roof_deck_thickness',
            'oc_house_roof_deck_vol', 'oc_house_total_sbf',
            'oc_sound_batts', 'oc_garage_walls', 'oc_garage_roof_deck',
            'oc_garage_total_sbf', 'oc_sets', 'oc_mtr_cost',
            'oc_man_hours', 'oc_shifts', 'oc_incedentals',
            'oc_sprayer_cost', 'oc_labor_cost', 'oc_total_cost',
            'oc_total_price', 'oc_profit', 'oc_margins',
            'oc_commission', 'oc_profit_after_com',

            # Hybrid
            'hy_ext_house_walls_sqft', 'hy_wall_thickness',
            'hy_house_roof_deck_sqft', 'hy_house_roof_deck_thickness',
            'hy_house_roof_deck_vol', 'hy_house_total_sbf',
            'hy_sound_batts', 'hy_garage_walls', 'hy_garage_roof_deck',
            'hy_garage_total_sbf', 'hy_sets', 'hy_mtr_cost',
            'hy_man_hours', 'hy_shifts', 'hy_incedentals',
            'hy_sprayer_cost', 'hy_labor_cost', 'hy_total_cost',
            'hy_total_price', 'hy_profit', 'hy_margins',
            'hy_commission', 'hy_profit_after_com',

            # Fiberglass
            'fg_labor_sqft', 'fg_cost_sqft', 'fg_profit_sqft',

            # Cathedral
            'cd_labor_sqft', 'cd_cost_sqft', 'cd_profit_sqft',

            # Blow In
            'bi_labor_sqft', 'bi_cost_sqft', 'bi_profit_sqft',

            # Attic
            'cc_attic_floor_sqft', 'cc_attic_inches_thick',

            # Auto-calculated
            'ext_house_walls_units', 'house_roof_deck_units',
            'house_total_sbf', 'garage_total_sbf',
            'sets_oc', 'sets_cc', 'sets_hybrid'
        ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['readonly_metrics'] = generate_readonly_fields_html(self.get_form(), ['oc', 'cc', 'hy'])
        return context
        return context
    def form_valid(self, form):
        obj = form.save(commit=False)

        # Constants
        BF_PER_SET = 15000
        SET_COST = 1625
        COMMISSION_RATE = 0.12
        PPU = {
            'oc': 0.34,  # Open Cell
            'cc': 1.80,  # Closed Cell
            'hy': 2.65,  # Hybrid
        }

        for prefix in ['oc', 'cc', 'hy']:
            # === Inputs from form ===
            sqft_roof = form.cleaned_data.get(f'{prefix}_house_roof_deck_sqft', 0) or 0
            thick_roof = form.cleaned_data.get(f'{prefix}_house_roof_deck_thickness', 0) or 0
            sqft_walls = form.cleaned_data.get(f'{prefix}_ext_house_walls_sqft', 0) or 0
            thick_walls = form.cleaned_data.get(f'{prefix}_wall_thickness', 0) or 0

            # === Core Calculations ===
            roof_vol = sqft_roof * thick_roof
            wall_units = sqft_walls * thick_walls
            total_sbf = roof_vol + wall_units
            sets = total_sbf / BF_PER_SET if BF_PER_SET else 0
            mtr_cost = sets * SET_COST
            ppu = PPU.get(prefix, 0)
            total_price = total_sbf * ppu
            profit = total_price - mtr_cost

            # === Profitability Metrics ===
            margin = (profit / total_price) if total_price > 0 else 0
            commission = total_price * COMMISSION_RATE
            profit_after_com = profit - commission

            # === Save to object ===
            setattr(obj, f'{prefix}_house_roof_deck_vol', roof_vol)
            setattr(obj, f'{prefix}_house_total_sbf', total_sbf)
            setattr(obj, f'{prefix}_sets', sets)
            setattr(obj, f'{prefix}_mtr_cost', mtr_cost)
            setattr(obj, f'{prefix}_total_price', total_price)
            setattr(obj, f'{prefix}_profit', profit)
            setattr(obj, f'{prefix}_margins', margin)
            setattr(obj, f'{prefix}_commission', commission)
            setattr(obj, f'{prefix}_profit_after_com', profit_after_com)

        obj.save()
        return super().form_valid(form)

from django.views.generic import TemplateView
from django.utils.timezone import now, timedelta
from .models import SprayFoamCalculation
from django.db.models import Avg, Count

class HomeDashboardView(TemplateView):
    template_name = 'projects/home_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thirty_days_ago = now() - timedelta(days=30)

        context["recent_quotes_count"] = SprayFoamCalculation.objects.filter(
            created_at__gte=thirty_days_ago
        ).count()

        context["average_profit"] = SprayFoamCalculation.objects.aggregate(
            avg_profit=Avg('cc_profit')  # You can choose oc/hy if preferred or calculate across all
        )['avg_profit'] or 0

        context["accepted_quotes_count"] = SprayFoamCalculation.objects.filter(
            is_accepted=True
        ).count()

        return context
