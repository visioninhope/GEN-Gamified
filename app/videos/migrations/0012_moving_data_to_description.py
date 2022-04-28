# Generated by Django 3.2.13 on 2022-04-28 16:26

from django.db import migrations


def move_data(apps, schema_editor):
    VideoFile = apps.get_model("videos", "VideoFile")
    for item in VideoFile.objects.all():
        item.description = item.content
        item.description_en = item.description
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0011_alter_videofile_internal_name"),
    ]

    operations = [migrations.RunPython(move_data)]
