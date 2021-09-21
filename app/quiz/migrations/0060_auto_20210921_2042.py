# Generated by Django 3.1.13 on 2021-09-21 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0063_auto_20210904_1823'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0059_auto_20210918_1859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionattempt',
            options={'ordering': ['created'], 'verbose_name': 'question attempt', 'verbose_name_plural': 'question attempts'},
        ),
        migrations.AddField(
            model_name='questionattempt',
            name='quiz_score',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizscore', verbose_name='quiz submission'),
        ),
        migrations.AddField(
            model_name='quizscore',
            name='max_mistakes',
            field=models.PositiveIntegerField(default=0, help_text='If the participant exceeds this value, the quiz is marked as failed', verbose_name='maximum number of mistakes'),
        ),
        migrations.AddField(
            model_name='quizscore',
            name='min_percentage',
            field=models.PositiveIntegerField(default=80, help_text='If the participant score percentage is below this value, the quiz is marked as failed', verbose_name='minimum percentage acceptable'),
        ),
        migrations.AlterUniqueTogether(
            name='quizscore',
            unique_together={('student', 'course', 'quiz', 'attempt_number')},
        ),
    ]
