from django.db import migrations


def seed_questions(apps, schema_editor):
    Question = apps.get_model('quiz', 'Question')
    # Avoid duplicating data if this migration is ever re-run against a
    # database that already has questions in it.
    if Question.objects.exists():
        return

    from quiz.questions_data import QUESTIONS

    for i, q in enumerate(QUESTIONS):
        Question.objects.create(
            outcome_code=q['outcome_code'],
            outcome_label=q['outcome_label'],
            text=q['text'],
            options=q['options'],
            correct_index=q['correct_index'],
            order=i,
        )


def remove_questions(apps, schema_editor):
    Question = apps.get_model('quiz', 'Question')
    Question.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_questions, remove_questions),
    ]
