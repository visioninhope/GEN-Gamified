# Generated by Django 4.0.4 on 2022-06-04 01:24

import core.support_methods
import upload_validator

import django.db.models.deletion
import GEN.storage_backends
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("scorm", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="scormobject",
            name="url",
        ),
        migrations.AddField(
            model_name="scormobject",
            name="package_id",
            field=models.CharField(
                blank=True,
                help_text="Identifier used by SCORM Cloud to refer to the package (note that  SCORM Cloud uses the terms 'package' and 'course' interchangeably).",
                max_length=255,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="scormobject",
            name="file",
            field=models.FileField(
                help_text="Format accepted: zip.",
                storage=GEN.storage_backends.PrivateMediaStorage(),
                upload_to=core.support_methods.user_directory_path_not_random,
                validators=[
                    upload_validator.FileTypeValidator(
                        allowed_types=["application/zip"]
                    )
                ],
                verbose_name="SCORM package",
            ),
        ),
        migrations.CreateModel(
            name="ScormRegistration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("registration_id", models.CharField(max_length=255, unique=True)),
                (
                    "learner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "package_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="scorm.scormobject",
                    ),
                ),
            ],
        ),
    ]
