# Generated by Django 4.2.5 on 2023-09-26 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='images',
            field=models.ImageField(upload_to='jobs_images/', verbose_name='이미지'),
        ),
    ]
