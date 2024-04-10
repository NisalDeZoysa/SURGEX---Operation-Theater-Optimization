# Generated by Django 4.0.1 on 2022-02-04 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('NIC', models.SlugField()),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('BMI', models.FloatField()),
                ('situation', models.FloatField()),
                ('seriousness', models.FloatField()),
                ('surgery_type', models.IntegerField()),
                ('time_slots', models.IntegerField()),
                ('surgeons', models.IntegerField()),
                ('urgancy', models.IntegerField()),
                ('category', models.IntegerField()),
                ('nature_of_surgery', models.IntegerField()),
                ('date_of_visit_day', models.IntegerField()),
                ('date_of_visit_month', models.IntegerField()),
                ('date_of_visit_year', models.IntegerField()),
                ('oparation_deadline_day', models.IntegerField()),
                ('oparation_deadline_month', models.IntegerField()),
                ('oparation_deadline_year', models.IntegerField()),
                ('veto_days_day', models.IntegerField(null=True)),
                ('veto_days_month', models.IntegerField(null=True)),
                ('veto_days_year', models.IntegerField(null=True)),
                ('surgery_time', models.FloatField()),
                ('surgery_date_day', models.IntegerField()),
                ('surgery_date_month', models.IntegerField()),
                ('surgery_date_year', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('NIC', models.SlugField()),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('BMI', models.FloatField()),
                ('situation', models.FloatField()),
                ('seriousness', models.FloatField()),
                ('surgery_type', models.IntegerField()),
                ('time_slots', models.IntegerField()),
                ('surgeons', models.IntegerField()),
                ('urgancy', models.IntegerField()),
                ('category', models.IntegerField()),
                ('nature_of_surgery', models.IntegerField()),
                ('date_of_visit_day', models.IntegerField()),
                ('date_of_visit_month', models.IntegerField()),
                ('date_of_visit_year', models.IntegerField()),
                ('oparation_deadline_day', models.IntegerField()),
                ('oparation_deadline_month', models.IntegerField()),
                ('oparation_deadline_year', models.IntegerField()),
                ('veto_days_day', models.IntegerField(null=True)),
                ('veto_days_month', models.IntegerField(null=True)),
                ('veto_days_year', models.IntegerField(null=True)),
                ('surgery_time', models.FloatField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('NIC', models.SlugField()),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('BMI', models.FloatField()),
                ('situation', models.FloatField()),
                ('seriousness', models.FloatField()),
                ('surgery_type', models.IntegerField()),
                ('time_slots', models.IntegerField()),
                ('surgeons', models.IntegerField()),
                ('urgancy', models.IntegerField()),
                ('category', models.IntegerField()),
                ('nature_of_surgery', models.IntegerField()),
                ('date_of_visit_day', models.IntegerField()),
                ('date_of_visit_month', models.IntegerField()),
                ('date_of_visit_year', models.IntegerField()),
                ('oparation_deadline_day', models.IntegerField()),
                ('oparation_deadline_month', models.IntegerField()),
                ('oparation_deadline_year', models.IntegerField()),
                ('veto_days_day', models.IntegerField(null=True)),
                ('veto_days_month', models.IntegerField(null=True)),
                ('veto_days_year', models.IntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
