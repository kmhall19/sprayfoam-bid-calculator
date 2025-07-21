# accounts/forms.py
from django import forms
from .models import CostSettings

class CostSettingsForm(forms.ModelForm):
    class Meta:
        model = CostSettings
        fields = [
                    'user',
                    'material_cost_open_cell',
                    'material_cost_closed_cell',
                    'labor_cost_per_sqft',
                    'equipment_overhead',
                    'default_profit_margin',
                    'oc_ppu',##
                    'cc_ppu',##
                    'hy_ppu',##
                    'fg_labor_per_sqft',##
                    'fg_exp_prof_sqft',
                    'bi_lb_brd_foot',##
                    'bi_exp_prof_brd_foot',
                    'labor_sqft',#
                    'def_comm_rate',##
                    'cd_exp_prof_sqft',
                    'cd_labor_per_sqft',#
                    'set_of_oc_cost',
                    'set_of_oc_exp_yld',
                    'set_of_cc_cost',
                    'set_of_cc_exp_yld',
                    'roll_of_batts_ext_cost',
                    'roll_of_batts_ext_exp_yld',
                    'roll_of_batts_int_cost',
                    'roll_of_batts_int_exp_yld',
                    'roll_of_batts_cd_cost',
                    'roll_of_batts_cd_exp_yld',
                    'bi_bale_cost',
                    'bi_bale_exp_yld',
                    'plastic_cost',
                    'plastic_exp_yld',
                    'tape_cost',
                    'tape_exp_yld',
                    'oc_ir_hr',
                    'cc_ir_hr',
                    'roll_of_batts_ext_ir_hr',
                    'roll_of_batts_int_ir_hr',
                    'roll_of_batts_cd_ir_hr',
                    'bi_ir_hr',
                    'oc_comm_rate',
                    'cc_comm_rate',
                    'roll_of_batts_ext_comm_rate',
                    'roll_of_batts_int_comm_rate',
                    'roll_of_batts_cd_comm_rate',
                    'rig_fuel_rate',
                    'consum_per_diem',
                    'hotel_per_diem',
                    'hrs_per_shift'
        ]
        widgets = {
            field: forms.NumberInput(attrs={'class': 'form-control'})
            for field in fields
        }
