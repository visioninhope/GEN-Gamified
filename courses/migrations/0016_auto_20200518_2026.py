# Generated by Django 3.0.3 on 2020-05-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20200518_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionitem',
            name='description',
            field=models.CharField(help_text='Course description (max 200 characters)', max_length=200),
        ),
    ]
