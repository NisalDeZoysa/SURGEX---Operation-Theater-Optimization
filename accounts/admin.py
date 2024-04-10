from django.contrib import admin
from .models import Patient_final


class patient_input(admin.ModelAdmin):
    list_display = ('user', 'name', 'NIC', 'age' )
    list_filter = []
    search_fields = ['user']

admin.site.register(Patient_final, patient_input)

# Register your models here.
