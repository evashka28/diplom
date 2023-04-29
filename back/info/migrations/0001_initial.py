# Generated by Django 3.2.18 on 2023-04-27 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('surname', models.CharField(blank=True, max_length=255, verbose_name='surname')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='mobile')),
                ('birth', models.DateField(blank=True, max_length=255, null=True, verbose_name='bithday')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('room', models.IntegerField(verbose_name='room')),
                ('mon', models.CharField(max_length=255)),
                ('tue', models.CharField(max_length=255)),
                ('wed', models.CharField(max_length=255)),
                ('thu', models.CharField(max_length=255)),
                ('fri', models.CharField(max_length=255)),
                ('sat', models.CharField(max_length=255)),
                ('sun', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_date', models.DateTimeField(max_length=255, verbose_name='date')),
                ('diagnosis', models.CharField(max_length=255, verbose_name='diagnosis')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.patient')),
            ],
        ),
    ]