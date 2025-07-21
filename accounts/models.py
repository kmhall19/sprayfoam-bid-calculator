from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class CostSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    material_cost_open_cell = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    material_cost_closed_cell = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    labor_cost_per_sqft = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    equipment_overhead = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    default_profit_margin = models.DecimalField(max_digits=5, decimal_places=2, default=20)

    oc_ppu = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    cc_ppu = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    hy_ppu = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    
    fg_labor_per_sqft = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    fg_exp_prof_sqft = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    
    bi_lb_brd_foot = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    bi_exp_prof_brd_foot = models.DecimalField(max_digits=8,decimal_places=2, default=0)

    labor_sqft = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    def_comm_rate = models.DecimalField(max_digits=8,decimal_places=2, default=0)

    cd_exp_prof_sqft = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    cd_labor_per_sqft = models.DecimalField(max_digits=8,decimal_places=2, default=0)

    set_of_oc_cost = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    set_of_oc_exp_yld = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    set_of_cc_cost = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    set_of_cc_exp_yld = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_ext_cost = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_ext_exp_yld = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_int_cost = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_int_exp_yld = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_cd_cost = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_cd_exp_yld = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    bi_bale_cost = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    bi_bale_exp_yld = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    plastic_cost  = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    plastic_exp_yld = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    tape_cost = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    tape_exp_yld = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    oc_ir_hr = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    cc_ir_hr = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_ext_ir_hr = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_int_ir_hr = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_cd_ir_hr = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    bi_ir_hr = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    oc_comm_rate = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    cc_comm_rate = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_ext_comm_rate = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_int_comm_rate = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    roll_of_batts_cd_comm_rate = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    rig_fuel_rate = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    consum_per_diem = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    hotel_per_diem = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    hrs_per_shift = models.DecimalField(max_digits=8,decimal_places=2, default=0)
    


    ## Material Costs

    ## Material Yields

    ## Incidentals

    ## Install Rates

    ## Sales Commissions


    def __str__(self):
        return f"Cost Settings for {self.user.username}"
