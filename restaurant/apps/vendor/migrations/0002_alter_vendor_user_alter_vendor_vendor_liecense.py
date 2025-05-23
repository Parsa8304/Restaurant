# Generated by Django 5.2 on 2025-05-08 09:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_liecense',
            field=models.FileField(unique=True, upload_to='vendor/liecense'),
        ),
    ]
