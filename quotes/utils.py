from .models import Quote
from projects.models import Measurements
from accounts.models import CostSettings

def calculate_quote_for_project(project):
    measurements = project.measurements
    settings = CostSettings.objects.get(user=project.user)

    area = measurements.length * measurements.width  # Simplified — could adjust for pitch
    material_cost = area * (settings.material_cost_open_cell if measurements.insulation_type == "open_cell" else settings.material_cost_closed_cell)
    labor_cost = area * settings.labor_cost_per_sqft
    equipment_cost = settings.equipment_overhead
    overhead_cost = 0  # Placeholder
    total_cost = material_cost + labor_cost + equipment_cost + overhead_cost
    final_bid = total_cost * (1 + settings.default_profit_margin / 100)

    quote, created = Quote.objects.update_or_create(
        project=project,
        defaults={
            'spray_area': area,
            'material_cost': material_cost,
            'labor_cost': labor_cost,
            'equipment_cost': equipment_cost,
            'overhead_cost': overhead_cost,
            'total_cost': total_cost,
            'profit_margin': settings.default_profit_margin,
            'final_bid': final_bid,
        }
    )
    return quote
