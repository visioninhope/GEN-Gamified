# Generated by Django 4.0.4 on 2022-06-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0084_alter_sectionitem_item_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section",
            name="section_type",
            field=models.CharField(
                choices=[
                    ("D", "Discussion boards"),
                    ("V", "Videos"),
                    ("Q", "Quizzes"),
                    ("U", "Uploads"),
                    ("C", "Content"),
                    ("S", "SCORM"),
                ],
                max_length=1,
                verbose_name="section type",
            ),
        ),
    ]
