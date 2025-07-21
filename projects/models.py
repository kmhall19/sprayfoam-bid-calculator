from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Location/Address Information
    location = models.CharField(max_length=255, blank=True, null=True)
    client_address_1 = models.CharField(max_length=255, blank=True, null=True)
    client_address_2 = models.CharField(max_length=255, blank=True, null=True)
    client_city = models.CharField(max_length=255, blank=True, null=True)
    client_state = models.CharField(max_length=255, blank=True, null=True)
    client_country = models.CharField(max_length=255, blank=True, null=True)
    client_lat = models.CharField(max_length=255, blank=True, null=True)
    client_long = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.CharField(max_length=255, blank=True, null=True)
    duration = models.FloatField(default = 0)
    client_zip =  models.FloatField(default= 0)
    business_type = models.CharField(max_length=255, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.FloatField(default= 1)

    def __str__(self):
        return self.name

class Measurements(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    # TESTING
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    roof_pitch = models.FloatField()
    insulation_type = models.CharField(max_length=50, choices=[
        ('open_cell', 'Open Cell'),
        ('closed_cell', 'Closed Cell')
    ])
    thickness = models.FloatField(default = 1)

    # ACTUAL
    roof_deck_width = models.FloatField(default = 1)
    peak_height = models.FloatField(default = 1)
    gable = models.FloatField(default = 1)
    eve_height = models.FloatField(default = 1)

    ## CLOSED CELL
    cc_wall_thickness = models.FloatField(default = 0)
    cc_roof_deck_thickness = models.FloatField(default = 0)
    cc_price_per_SBF = models.FloatField(default = 0)

    ## OPEN CELL
    oc_wall_thickness = models.FloatField(default = 0)
    oc_roof_deck_thickness = models.FloatField(default = 0)
    oc_price_per_SBF = models.FloatField(default = 0)

    ## HYBRID - OC + CC
    hy_wall_thickness = models.FloatField(default = 0)
    hy_roof_deck_thickness = models.FloatField(default = 0)
    hy_price_per_SBF = models.FloatField(default = 0)  

    ## DEDUCTIONS - Windows, Doors, Other
    i1_name = models.FloatField(default = 0)  
    i1_width = models.FloatField(default = 0)  
    i1_height = models.FloatField(default = 0)  
    i1_quantity = models.FloatField(default = 0)  

    i2_name = models.FloatField(default = 0)  
    i2_width = models.FloatField(default = 0)  
    i2_height = models.FloatField(default = 0)  
    i2_quantity = models.FloatField(default = 0)

    i3_name = models.FloatField(default = 0)  
    i3_width = models.FloatField(default = 0)  
    i3_height = models.FloatField(default = 0)  
    i3_quantity = models.FloatField(default = 0)

    def __str__(self):
        return f"Measurements for {self.project.name}"


# models.py
from django.db import models

class SprayFoamCalculation(models.Model):
    # Closed Cell
    cc_ppu = ''
    cc_ext_house_walls_sqft = models.FloatField()
    cc_wall_thickness = models.FloatField()
    cc_house_roof_deck_sqft = models.FloatField()
    cc_house_roof_deck_thickness = models.FloatField()
    cc_house_roof_deck_vol = models.FloatField()
    cc_house_total_sbf = models.FloatField()
    cc_sound_batts = models.FloatField()
    cc_garage_walls = models.FloatField()
    cc_garage_roof_deck = models.FloatField()
    cc_garage_total_sbf = models.FloatField()
    cc_sets = models.FloatField()
    cc_mtr_cost = models.FloatField()
    cc_man_hours = models.FloatField()
    cc_shifts = models.FloatField()
    cc_incedentals = models.FloatField()
    cc_sprayer_cost = models.FloatField()
    cc_labor_cost = models.FloatField()
    cc_total_cost = models.FloatField()
    cc_total_price = models.FloatField()
    cc_profit = models.FloatField()
    cc_margins = models.FloatField()
    cc_commission = models.FloatField()
    cc_profit_after_com = models.FloatField()

    #OPEN CELL
    oc_ppu = ''
    oc_ext_house_walls_sqft = models.FloatField()
    oc_wall_thickness = models.FloatField()
    oc_house_roof_deck_sqft = models.FloatField()
    oc_house_roof_deck_thickness = models.FloatField()
    oc_house_roof_deck_vol = models.FloatField()
    oc_house_total_sbf = models.FloatField()
    oc_sound_batts = models.FloatField()
    oc_garage_walls = models.FloatField()
    oc_garage_roof_deck = models.FloatField()
    oc_garage_total_sbf = models.FloatField()
    oc_sets = models.FloatField()
    oc_mtr_cost = models.FloatField()
    oc_man_hours = models.FloatField()
    oc_shifts = models.FloatField()
    oc_incedentals = models.FloatField()
    oc_sprayer_cost = models.FloatField()
    oc_labor_cost = models.FloatField()
    oc_total_cost = models.FloatField()
    oc_total_price = models.FloatField()
    oc_profit = models.FloatField()
    oc_margins = models.FloatField()
    oc_commission = models.FloatField()
    oc_profit_after_com = models.FloatField()

    #Hybrid
    hy_ppu = ''
    hy_ext_house_walls_sqft = models.FloatField()
    hy_wall_thickness = models.FloatField()
    hy_house_roof_deck_sqft = models.FloatField()
    hy_house_roof_deck_thickness = models.FloatField()
    hy_house_roof_deck_vol = models.FloatField()
    hy_house_total_sbf = models.FloatField()
    hy_sound_batts = models.FloatField()
    hy_garage_walls = models.FloatField()
    hy_garage_roof_deck = models.FloatField()
    hy_garage_total_sbf = models.FloatField()
    hy_sets = models.FloatField()
    hy_mtr_cost = models.FloatField()
    hy_man_hours = models.FloatField()
    hy_shifts = models.FloatField()
    hy_incedentals = models.FloatField()
    hy_sprayer_cost = models.FloatField()
    hy_labor_cost = models.FloatField()
    hy_total_cost = models.FloatField()
    hy_total_price = models.FloatField()
    hy_profit = models.FloatField()
    hy_margins = models.FloatField()
    hy_commission = models.FloatField()
    hy_profit_after_com = models.FloatField()

    # FIBERGLASS
    fg_labor_sqft = models.FloatField()
    fg_cost_sqft = models.FloatField()
    fg_profit_sqft = models.FloatField()

    # CATHEDRAL
    cd_labor_sqft = models.FloatField()
    cd_cost_sqft = models.FloatField()
    cd_profit_sqft = models.FloatField()


    # BLOW IN
    bi_labor_sqft = models.FloatField()
    bi_cost_sqft = models.FloatField()
    bi_profit_sqft = models.FloatField()

    cc_attic_floor_sqft = models.FloatField(null=True, blank=True)
    cc_attic_inches_thick = models.FloatField(null=True, blank=True)
    
    # ... Add all white cell fields

    # Auto-calculated results (gray fields)
    ext_house_walls_units = models.FloatField(blank=True, null=True)
    house_roof_deck_units = models.FloatField(blank=True, null=True)
    house_total_sbf = models.FloatField(blank=True, null=True)
    garage_total_sbf = models.FloatField(blank=True, null=True)
    sets_oc = models.FloatField(blank=True, null=True)
    sets_cc = models.FloatField(blank=True, null=True)
    sets_hybrid = models.FloatField(blank=True, null=True)
    # etc.

    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)