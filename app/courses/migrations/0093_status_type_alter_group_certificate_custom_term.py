# Generated by Django 4.0.10 on 2023-04-13 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0092_alter_course_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="status",
            name="type",
            field=models.CharField(
                choices=[
                    ("G", "Group"),
                    ("C", "Course"),
                    ("S", "Section"),
                    ("N", "None"),
                ],
                default="N",
                help_text="Sets what kind of object the status is related to: group, course, or section.",
                max_length=1,
                verbose_name="status type",
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="certificate_custom_term",
            field=models.CharField(
                blank=True,
                help_text="Certificate custom term to be used instead of the group name. Max length: 200 characters.",
                max_length=200,
                verbose_name="certificate custom term",
            ),
        ),
    ]
