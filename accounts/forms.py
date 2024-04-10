from dataclasses import fields
from django.forms import ModelForm
from articles.models import Patient

class patient_form(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'