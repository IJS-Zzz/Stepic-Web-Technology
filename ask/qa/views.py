from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from models import Answer, Question
from forms import AskForm, AnswerForm, SignupForm, LoginForm


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
    if request.user.is_authenticated:
        user = request.user
    else:
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
    if request.user.is_authenticated:
        user = request.user
    else:
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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {'form': form,
                                            'user': request.user,
                                            'session': request.session, })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.raw_password
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    return render(request, 'qa/signup.html', {'form': form,
                                           'user': request.user,
                                           'session': request.session, })









