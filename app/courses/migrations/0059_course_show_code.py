# Generated by Django 3.1.13 on 2021-07-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0058_auto_20210729_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='show_code',
            field=models.BooleanField(default=False, help_text='Show course code to instructors.', verbose_name='show course code'),
        ),
    ]
