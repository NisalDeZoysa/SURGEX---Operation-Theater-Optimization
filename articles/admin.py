from django.contrib import admin
from .models import Patient, Patient_duration, Patient_test


class patient_input(admin.ModelAdmin):
    list_display = ('user', 'name', 'NIC', 'age' )
    list_filter = []
    search_fields = ['user']


admin.site.site_header = 'Eximius Ruhuna'
admin.site.register(Patient, patient_input)
admin.site.register(Patient_duration, patient_input)
admin.site.register(Patient_test, patient_input)




# Register your models here.
