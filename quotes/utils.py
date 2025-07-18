from .models import Quote
from projects.models import Measurements
from accounts.models import CostSettings
from decimal import Decimal

def calculate_quote_for_project(project):
    measurements = project.measurements
    settings, _ = CostSettings.objects.get_or_create(user=project.user)

    # Convert float to Decimal for compatibility
    area = Decimal(measurements.length * measurements.width)

    material_rate = (
        settings.material_cost_open_cell
        if measurements.insulation_type == 'open_cell'
        else settings.material_cost_closed_cell
    )

    material_cost = area * material_rate
    labor_cost = area * settings.labor_cost_per_sqft
    equipment_cost = settings.equipment_overhead
    overhead_cost = Decimal("0.00")
    total_cost = material_cost + labor_cost + equipment_cost + overhead_cost
    final_bid = total_cost * (1 + settings.default_profit_margin / Decimal("100"))

    quote, _ = Quote.objects.update_or_create(
        project=project,
        defaults={
            'spray_area': float(area),
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

