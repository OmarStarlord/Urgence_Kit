from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Tip, NutrimentAndSupply, EmergencyContact

@admin.register(Tip)
class TipAdmin(ImportExportModelAdmin):
    pass

@admin.register(NutrimentAndSupply)
class NutrimentAndSupplyAdmin(ImportExportModelAdmin):
    pass

@admin.register(EmergencyContact)
class EmergencyContactAdmin(ImportExportModelAdmin):
    pass


