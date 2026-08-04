from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome_code', models.CharField(help_text="e.g. 'OUTCOME 1' — used to group questions for the breakdown.", max_length=32)),
                ('outcome_label', models.CharField(help_text="Full topic label shown above the question, e.g. 'OUTCOME 1 · PYTHON FUNDAMENTALS'.", max_length=120)),
                ('text', models.TextField(help_text='The question text. Use \\n for line breaks.')),
                ('options', models.JSONField(help_text='List of 2-4 answer option strings.')),
                ('correct_index', models.PositiveSmallIntegerField(help_text="Zero-based index into 'options' that is the correct answer.")),
                ('order', models.PositiveIntegerField(default=0, help_text='Display order in the quiz.')),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('score', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('answers', models.JSONField(help_text='List of selected option indices (or null if skipped), in question order.')),
                ('breakdown', models.JSONField(help_text="Per-outcome correct/total counts, e.g. {'OUTCOME 1': {'correct': 2, 'total': 3}, ...}")),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-submitted_at'],
            },
        ),
    ]
