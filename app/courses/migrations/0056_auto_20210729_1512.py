# Generated by Django 3.1.13 on 2021-07-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0055_course_provide_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(help_text='Course name (max 150 characters)', max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name_en',
            field=models.CharField(help_text='Course name (max 150 characters)', max_length=150, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name_fr',
            field=models.CharField(help_text='Course name (max 150 characters)', max_length=150, null=True, verbose_name='name'),
        ),
    ]
