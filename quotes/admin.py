from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("project", "final_bid", "profit_margin", "date_generated")
