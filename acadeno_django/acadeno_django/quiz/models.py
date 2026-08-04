from django.db import models


class Question(models.Model):
    """A single multiple-choice question mapped to one programme outcome."""

    outcome_code = models.CharField(
        max_length=32,
        help_text="e.g. 'OUTCOME 1' — used to group questions for the breakdown."
    )
    outcome_label = models.CharField(
        max_length=120,
        help_text="Full topic label shown above the question, e.g. "
                   "'OUTCOME 1 · PYTHON FUNDAMENTALS'."
    )
    text = models.TextField(help_text="The question text. Use \\n for line breaks.")
    options = models.JSONField(help_text="List of 2-4 answer option strings.")
    correct_index = models.PositiveSmallIntegerField(
        help_text="Zero-based index into 'options' that is the correct answer."
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order in the quiz.")

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"[{self.outcome_code}] {self.text[:60]}"


class Submission(models.Model):
    """A learner's completed run through the outcomes check."""

    name = models.CharField(max_length=200)
    score = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    answers = models.JSONField(
        help_text="List of selected option indices (or null if skipped), "
                   "in question order."
    )
    breakdown = models.JSONField(
        help_text="Per-outcome correct/total counts, e.g. "
                   "{'OUTCOME 1': {'correct': 2, 'total': 3}, ...}"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} — {self.score}/{self.total}"

    @property
    def percent(self):
        if not self.total:
            return 0
        return round((self.score / self.total) * 100)
