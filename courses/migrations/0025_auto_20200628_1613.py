# Generated by Django 3.0.7 on 2020-06-28 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_auto_20200628_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='participant',
            new_name='participants',
        ),
    ]
