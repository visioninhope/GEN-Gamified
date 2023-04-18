# Generated by Django 4.0.10 on 2023-04-13 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0093_status_type_alter_group_certificate_custom_term"),
    ]

    operations = [
        migrations.AddField(
            model_name="status",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="status",
                to="courses.group",
            ),
        ),
        migrations.AlterField(
            model_name="status",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="status",
                to="courses.course",
                verbose_name="course",
            ),
        ),
    ]
