from django.core.management.base import BaseCommand
from quiz.models import Question
from quiz.questions_data import QUESTIONS


class Command(BaseCommand):
    help = "Wipe and reseed the Question table from quiz/questions_data.py"

    def handle(self, *args, **options):
        Question.objects.all().delete()
        for i, q in enumerate(QUESTIONS):
            Question.objects.create(
                outcome_code=q['outcome_code'],
                outcome_label=q['outcome_label'],
                text=q['text'],
                options=q['options'],
                correct_index=q['correct_index'],
                order=i,
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(QUESTIONS)} questions."))
