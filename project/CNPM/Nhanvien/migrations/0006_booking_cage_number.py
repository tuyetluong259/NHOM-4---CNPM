# Generated by Django 5.1.4 on 2025-02-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nhanvien', '0005_booking_fee_amount_booking_is_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='cage_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
