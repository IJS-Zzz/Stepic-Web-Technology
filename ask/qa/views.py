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
    user = User.objects.first()

    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = user
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'qa/ask.html', {'form': form,
                                           'user': request.user,
                                           'session': request.session, })


def question(request, id):
    user = User.objects.first()

    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = user
            form.save()
            return HttpResponseRedirect(question.get_absolute_url())
    else:
        form = AnswerForm(initial={'question': question.id})

    return render(request, 'qa/question.html', {'question': question,
                                                'form': form,
                                                'user': request.user,
                                                'session': request.session, })
