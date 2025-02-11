# Generated by Django 5.1.6 on 2025-02-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_slider_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_site', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='images/')),
                ('email', models.CharField(max_length=100)),
                ('time_to_work', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'настройки',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
