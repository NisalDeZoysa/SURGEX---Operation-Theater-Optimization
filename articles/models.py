from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    NIC = models.SlugField()
    age = models.IntegerField()
    gender = models.IntegerField()
    BMI = models.FloatField()
    situation = models.FloatField()
    seriousness = models.FloatField()
    surgery_type = models.IntegerField()
    time_slots = models.IntegerField()
    surgeons = models.IntegerField()
    urgancy = models.IntegerField()
    category = models.IntegerField()
    nature_of_surgery = models.IntegerField()
    date_of_visit_day = models.IntegerField()
    date_of_visit_month = models.IntegerField()
    date_of_visit_year = models.IntegerField()
    oparation_deadline_day = models.IntegerField()
    oparation_deadline_month = models.IntegerField()
    oparation_deadline_year = models.IntegerField()
    veto_days_day = models.IntegerField(null=True)
    veto_days_month = models.IntegerField(null=True)
    veto_days_year = models.IntegerField(null=True)




    def __str__(self):
        return self.name


class Patient_duration(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    NIC = models.SlugField()
    age = models.IntegerField()
    gender = models.IntegerField()
    BMI = models.FloatField()
    situation = models.FloatField()
    seriousness = models.FloatField()
    surgery_type = models.IntegerField()
    time_slots = models.IntegerField()
    surgeons = models.IntegerField()
    urgancy = models.IntegerField()
    category = models.IntegerField()
    nature_of_surgery = models.IntegerField()
    date_of_visit_day = models.IntegerField()
    date_of_visit_month = models.IntegerField()
    date_of_visit_year = models.IntegerField()
    oparation_deadline_day = models.IntegerField()
    oparation_deadline_month = models.IntegerField()
    oparation_deadline_year = models.IntegerField()
    veto_days_day = models.IntegerField(null=True)
    veto_days_month = models.IntegerField(null=True)
    veto_days_year = models.IntegerField(null=True)
    surgery_time = models.FloatField()


    def __str__(self):
        return self.name


class Patient_test(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    NIC = models.SlugField()
    age = models.IntegerField()
    gender = models.IntegerField()
    BMI = models.FloatField()
    situation = models.FloatField()
    seriousness = models.FloatField()
    surgery_type = models.IntegerField()
    time_slots = models.IntegerField()
    surgeons = models.IntegerField()
    urgancy = models.IntegerField()
    category = models.IntegerField()
    nature_of_surgery = models.IntegerField()
    date_of_visit_day = models.IntegerField()
    date_of_visit_month = models.IntegerField()
    date_of_visit_year = models.IntegerField()
    oparation_deadline_day = models.IntegerField()
    oparation_deadline_month = models.IntegerField()
    oparation_deadline_year = models.IntegerField()
    veto_days_day = models.IntegerField(null=True)
    veto_days_month = models.IntegerField(null=True)
    veto_days_year = models.IntegerField(null=True)
    surgery_time = models.FloatField()
    surgery_date_day = models.IntegerField()
    surgery_date_month = models.IntegerField()
    surgery_date_year = models.IntegerField()


    def __str__(self):
        return self.name

