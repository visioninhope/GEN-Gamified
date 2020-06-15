# Generated by Django 3.0.7 on 2020-06-15 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20200615_1624'),
        ('videos', '0004_auto_20200610_1732'),
        ('quiz', '0016_auto_20200613_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['custom_order'], 'verbose_name': 'question', 'verbose_name_plural': 'questions'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'quiz', 'verbose_name_plural': 'quizzes'},
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(help_text='enter the content that you want displayed.', max_length=1000, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='question',
            name='custom_order',
            field=models.PositiveIntegerField(default=0, verbose_name='custom order'),
        ),
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, help_text='Explanation to be shown after the question has been answered.', verbose_name='explanation'),
        ),
        migrations.AlterField(
            model_name='question',
            name='multiple_correct_answers',
            field=models.BooleanField(default=False, help_text='Does this question have multiple correct answers (allow user to select multiple answer items)?', verbose_name='multiple correct answers'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('H', 'Header'), ('L', 'Likert'), ('O', 'Open ended'), ('M', 'Multiple choice')], max_length=1, verbose_name='question type'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.Quiz', verbose_name='quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='attempts_max_number',
            field=models.PositiveIntegerField(default=1, verbose_name='attempts max number'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='quizzes', to='courses.Course', verbose_name='course'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='quiz.Quiz', verbose_name='requirement'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='show_correct_answers',
            field=models.BooleanField(default=False, verbose_name='show correct answers'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='show_score',
            field=models.BooleanField(default=False, verbose_name='show score'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quizzes', to='videos.VideoFile', verbose_name='video'),
        ),
    ]
