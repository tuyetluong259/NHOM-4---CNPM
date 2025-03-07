# Generated by Django 5.1.4 on 2025-02-20 14:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KhachHang', '0004_alter_appointment_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='diagnosis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('NHAP_VIEN', 'Nhập viện'), ('XUAT_VIEN', 'Xuất viện'), ('DIEU_TRI', 'Đang điều trị'), ('CHUA_DIEU_TRI', 'Chưa điều trị')], default='CHUA_DIEU_TRI', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
