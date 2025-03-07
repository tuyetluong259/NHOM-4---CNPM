# Generated by Django 5.1.4 on 2025-02-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('pet_name', models.CharField(max_length=255)),
                ('pet_gender', models.CharField(max_length=10)),
                ('pet_condition', models.TextField()),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('doctor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('staff_notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
