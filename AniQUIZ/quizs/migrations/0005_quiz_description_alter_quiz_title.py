# Generated by Django 4.1.5 on 2023-02-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizs', '0004_results_dict_answers_delete_dict'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(default='none', max_length=128),
        ),
    ]
