# Generated by Django 5.1.6 on 2025-02-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='phone1',
            field=models.CharField(help_text='+996 503 277 372', max_length=20),
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone2',
            field=models.CharField(blank=True, help_text='+996 503 277 372', max_length=20, null=True),
        ),
    ]
