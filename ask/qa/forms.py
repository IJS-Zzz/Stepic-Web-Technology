from django import forms
from django.contrib.auth.models import User

from models import Answer, Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField()

    def clean_title(self):
        if self.cleaned_data['title'] in [q['title'] for q in Question.objects.values('title').distinct().all()]:
            raise forms.ValidationError(
                'Question with this title is already exists. Please change title.',
                code='duplicate title',
            )
        return self.cleaned_data['title']

    def save(self):
        user = User.objects.first()
        return Question.objects.create(author=user, **self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    # def clean(self):
    #     pass

    def save(self):
        return Answer(text=self.cleaned_data['text'])