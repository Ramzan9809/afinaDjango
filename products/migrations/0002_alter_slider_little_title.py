# Generated by Django 5.1.6 on 2025-02-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='little_title',
            field=models.CharField(max_length=100, null=True, verbose_name='Под заголовок'),
        ),
    ]
