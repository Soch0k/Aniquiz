# Generated by Django 4.1.5 on 2023-02-15 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizs.cateory'),
        ),
        migrations.AddField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizs.quiz'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizs.questions'),
        ),
    ]
