# Generated by Django 3.2.13 on 2022-04-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0008_moving_data_to_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contentitem",
            name="content",
        ),
        migrations.RemoveField(
            model_name="contentitem",
            name="content_en",
        ),
        migrations.RemoveField(
            model_name="contentitem",
            name="content_fr",
        ),
    ]
