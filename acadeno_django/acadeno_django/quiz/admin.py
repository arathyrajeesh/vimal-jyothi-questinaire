from django.contrib import admin
from .models import Question, Submission


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('order', 'outcome_code', 'text_preview', 'correct_index')
    list_filter = ('outcome_code',)
    ordering = ('order',)

    def text_preview(self, obj):
        return obj.text[:70]
    text_preview.short_description = 'Question'


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'total', 'percent', 'submitted_at')
    readonly_fields = ('name', 'score', 'total', 'answers', 'breakdown', 'submitted_at')
    ordering = ('-submitted_at',)

    def has_add_permission(self, request):
        return False
