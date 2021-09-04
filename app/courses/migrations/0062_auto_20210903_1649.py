# Generated by Django 3.1.13 on 2021-09-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0061_auto_20210903_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(help_text='Section name (max 25 characters)', max_length=25, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name_en',
            field=models.CharField(help_text='Section name (max 25 characters)', max_length=25, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name_fr',
            field=models.CharField(help_text='Section name (max 25 characters)', max_length=25, null=True, verbose_name='name'),
        ),
    ]
