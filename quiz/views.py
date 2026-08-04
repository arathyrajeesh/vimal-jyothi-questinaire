from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .models import Question, Submission

SESSION_NAME = 'quiz_name'
SESSION_ANSWERS = 'quiz_answers'
SESSION_CURRENT = 'quiz_current'
SESSION_DONE_NAME = 'done_name'
SESSION_STAFF_OK = 'staff_ok'


def _questions():
    """All questions in display order. Small table, so a plain list is fine."""
    return list(Question.objects.all())


def landing(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if not name:
            messages.error(request, "Please enter your name to begin.")
            return render(request, 'quiz/landing.html', {'name': name})

        if name.lower() == 'admin':
            request.session[SESSION_STAFF_OK] = True
            return redirect('quiz:staff_list')

        if Submission.objects.filter(name__iexact=name).exists():
            messages.error(request, f"Submission already exists for '{name}'. Only one attempt is allowed.")
            return render(request, 'quiz/landing.html', {'name': name})


        qs = _questions()
        request.session[SESSION_NAME] = name
        request.session[SESSION_ANSWERS] = [None] * len(qs)
        request.session[SESSION_CURRENT] = 0
        return redirect('quiz:quiz_question')

    total_students = Submission.objects.count()
    return render(request, 'quiz/landing.html', {'name': '', 'total_students': total_students})




def quiz_question(request):
    qs = _questions()
    total = len(qs)

    if not request.session.get(SESSION_NAME) or SESSION_ANSWERS not in request.session:
        return redirect('quiz:landing')

    answers = request.session[SESSION_ANSWERS]
    current = request.session.get(SESSION_CURRENT, 0)
    current = max(0, min(current, total - 1))

    if request.method == 'POST':
        nav = request.POST.get('nav')
        raw_answer = request.POST.get('answer')

        if raw_answer is not None and raw_answer != '':
            answers[current] = int(raw_answer)
            request.session[SESSION_ANSWERS] = answers

        if nav == 'back':
            request.session[SESSION_CURRENT] = max(0, current - 1)
            request.session.modified = True
            return redirect('quiz:quiz_question')

        if nav == 'next':
            if answers[current] is None:
                messages.error(request, "Please select an answer before continuing.")
            elif current == total - 1:
                return _finish_quiz(request, qs, answers)
            else:
                request.session[SESSION_CURRENT] = current + 1
                request.session.modified = True
                return redirect('quiz:quiz_question')

    question = qs[current]
    context = {
        'name': request.session.get(SESSION_NAME, ''),
        'question': question,
        'options': [
            {'idx': i, 'key': chr(65 + i), 'text': opt}
            for i, opt in enumerate(question.options)
        ],
        'selected': answers[current],
        'current': current,
        'index_display': current + 1,
        'total': total,
        'progress_pct': round((current / total) * 100) if total else 0,
        'is_last': current == total - 1,
        'has_back': current > 0,
    }
    return render(request, 'quiz/quiz.html', context)


def _finish_quiz(request, qs, answers):
    score = 0
    breakdown = {}
    for q, a in zip(qs, answers):
        bucket = breakdown.setdefault(q.outcome_code, {'correct': 0, 'total': 0})
        bucket['total'] += 1
        if a is not None and a == q.correct_index:
            bucket['correct'] += 1
            score += 1

    name = request.session.get(SESSION_NAME, '').strip()

    submission = Submission.objects.create(
        name=name,
        score=score,
        total=len(qs),
        answers=answers,
        breakdown=breakdown,
    )

    # Clear quiz-in-progress state, keep submission ID for the results page.
    for key in (SESSION_ANSWERS, SESSION_CURRENT, SESSION_NAME):
        request.session.pop(key, None)
    request.session[SESSION_DONE_NAME] = name
    request.session['done_submission_id'] = submission.id

    return redirect('quiz:done')


def done(request):
    name = request.session.get(SESSION_DONE_NAME)
    sub_id = request.session.get('done_submission_id')
    
    if not name or not sub_id:
        return redirect('quiz:landing')
        
    try:
        submission = Submission.objects.get(id=sub_id)
    except Submission.DoesNotExist:
        return redirect('quiz:landing')

    questions = list(Question.objects.all())
    question_results = []
    
    for idx, question in enumerate(questions):
        user_answer_idx = submission.answers[idx] if idx < len(submission.answers) else None
        
        options_detail = []
        for opt_idx, opt_text in enumerate(question.options):
            options_detail.append({
                'key': chr(65 + opt_idx),
                'text': opt_text,
                'is_correct': opt_idx == question.correct_index,
                'is_user_selected': opt_idx == user_answer_idx,
            })
            
        is_user_correct = (user_answer_idx == question.correct_index)
        
        question_results.append({
            'num': idx + 1,
            'question': question,
            'user_answer_idx': user_answer_idx,
            'is_correct': is_user_correct,
            'options': options_detail,
        })

    context = {
        'name': name,
        'submission': submission,
        'question_results': question_results,
    }
    return render(request, 'quiz/done.html', context)



def staff_gate(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        if code == settings.STAFF_ACCESS_CODE:
            request.session[SESSION_STAFF_OK] = True
            return redirect('quiz:staff_list')
        messages.error(request, "Incorrect access code — try again.")

    return render(request, 'quiz/admin_gate.html')


def staff_list(request):
    if not request.session.get(SESSION_STAFF_OK):
        return redirect('quiz:staff_gate')

    submissions = Submission.objects.all().order_by('-submitted_at')

    rows = []
    for sub in submissions:
        breakdown_display = "  ".join(
            f"{code.replace('OUTCOME ', 'O')}:{v['correct']}/{v['total']}"
            for code, v in sub.breakdown.items()
        )
        pct = sub.percent
        if pct >= 70:
            score_class = 'score-hi'
        elif pct >= 40:
            score_class = 'score-mid'
        else:
            score_class = 'score-lo'
        rows.append({
            'submission': sub,
            'pct': pct,
            'score_class': score_class,
            'breakdown_display': breakdown_display,
        })

    return render(request, 'quiz/admin_list.html', {'rows': rows, 'count': submissions.count()})


def staff_exit(request):
    request.session.pop(SESSION_STAFF_OK, None)
    return redirect('quiz:landing')
