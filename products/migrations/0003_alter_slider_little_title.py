# Generated by Django 5.1.6 on 2025-02-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_slider_little_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='little_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Под заголовок'),
        ),
    ]
