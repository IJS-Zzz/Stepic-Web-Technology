from django import forms
from django.contrib.auth.models import User

from models import Answer, Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        if self.cleaned_data['title'] in [q['title'] for q in Question.objects.values('title').distinct().all()]:
            raise forms.ValidationError(
                'Question with this title is already exists. Please change title.',
                code='duplicate title',
            )
        return self.cleaned_data['title']

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question

        # user = User.objects.first()
        # return Question.objects.create(author=user, **self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise forms.ValidationError(
                "Something's is going wrong! ",
                code='wrong question id',
            )
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer

        # return Answer(text=self.cleaned_data['text'])