# Generated by Django 5.0.4 on 2024-04-15 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer",
            old_name="answers",
            new_name="chosen_answer",
        ),
        migrations.AlterField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quizzes",
                to="survey.question",
            ),
        ),
    ]
