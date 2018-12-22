from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    #print(*args, **kwargs)
    return HttpResponse('OK')


def new_questions(request, *args, **kwargs):
    #print(*args, **kwargs)
    return HttpResponse('New Questions - OK\n')


def popular_questions(request, *args, **kwargs):
    #print(*args, **kwargs)
    return HttpResponse('Popular Questions - OK')


def question(request, *args, **kwargs):
    #print(*args, **kwargs)
    return HttpResponse('Question - OK')