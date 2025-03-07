# Generated by Django 5.1.4 on 2025-02-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nhanvien', '0003_alter_booking_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='diagnosis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='prescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('NHAP_VIEN', 'Nhập viện'), ('XUAT_VIEN', 'Xuất viện'), ('DIEU_TRI', 'Đang điều trị'), ('CHUA_DIEU_TRI', 'Chưa điều trị')], default='CHUA_DIEU_TRI', max_length=20),
        ),
    ]
