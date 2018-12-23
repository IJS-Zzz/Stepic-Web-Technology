from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.urls import reverse

from django.contrib.auth.models import User
from models import Answer, Question
from forms import AskForm, AnswerForm


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
    return render(request, 'qa/questions_list.html', {
        'page_title': "New Questions",
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


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
    return render(request, 'qa/questions_list.html', {
        'page_title': "Popular Questions",
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def ask(request):
    #### Test
    user_r = User.objects.first()
    user = request.user

    if request.method == "POST":
        # form = AskForm(request.POST, user=user_r)
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        # form = AskForm(user=user_r)
    return render(request, 'qa/ask.html', {
        'form': form,
    })


def question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        # request.POST['question'] = id
        form = AnswerForm(request.POST)
        if form.is_valid():
            new_answer = form.save()
            new_answer.author = User.objects.first()
            new_answer.question = question
            new_answer.save()
            form_posted = True
            return HttpResponseRedirect(question.get_absolute_url())
    else:
        form = AnswerForm()
    try:
        answers = question.answer_set.order_by('-id').all()
    except Answer.DoesNotExist:  # Need Test!
        answers = None
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })
