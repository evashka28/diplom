# Generated by Django 3.2.18 on 2023-05-31 15:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', help_text='Phone number must not contain spaces, letters, parentheses or dashes. It must contain 11 digits.', max_length=11, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must not contain spaces, letters, parentheses or dashes. It must contain 10 digits.', regex='^\\d{10}$')])),
                ('want_reminder', models.BooleanField(default=False)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('amount_to_pay', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('id_request', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_duration', models.PositiveIntegerField(default=30, help_text='Duration of each slot in minutes')),
                ('lead_time', models.TimeField(default='09:00', help_text='Time when slots start')),
                ('finish_time', models.TimeField(default='16:30', help_text='Time when we stop working')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.DurationField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('down_payment', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('currency', models.CharField(default='USD', max_length=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('id_request', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.service')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointmentrequest'),
        ),
    ]
