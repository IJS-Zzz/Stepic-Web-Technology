from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.urls import reverse

from models import Answer, Question


def test(request, *args, **kwargs):
    #print(*args, **kwargs)
    return HttpResponse('OK')


@require_GET
def new_questions(request):
    questions = Question.objects.new()
    try:
        limit = int(request.GET.get('limit', 10))
        if not 0 < limit <= 100:
            limit = 10
    except ValueError:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = reverse('qa:new') + '?page='
    page = paginator.page(page)
    return render(request, 'qa/questions.html', {
        'page_title': "New Questions",
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

    # questions = Question.paginate(request, Question.objects.new())
    # return render(request, 'qa/new_questions.html', {
    #     'questions': question,
    # })


@require_GET
def popular_questions(request):
    questions = Question.objects.popular()
    try:
        limit = int(request.GET.get('limit', 10))
        if not 0 < limit <= 100:
            limit = 10
    except ValueError:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = reverse('qa:popular') + '?page='
    page = paginator.page(page)
    return render(request, 'qa/questions.html', {
        'page_title': "Popular Questions",
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

    # questions = Question.paginate(request, Question.objects.popular())
    # return render(request, 'qa/popular_questions.html', {
    #     'questions': question,
    # })


@require_GET
def question(request, id):
    question = get_object_or_404(Question, id=id)
    try:
        answers = question.answer_set.all()
    except Answer.DoesNotExist:  # Need Test!
        answers = None
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
    })
