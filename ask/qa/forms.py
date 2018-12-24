from django import forms

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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


class SignupForm(forms.Form):
    username = forms.CharField(label='Your Username')
    email = forms.EmailField(label='Your Email')
    password = forms.CharField(label='Your Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError('Please Input Username.')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('Username is already taken!')
        except User.DoesNotExist:
            pass
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise form.ValidationError('Please Input Email.')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password:
            raise form.ValidationError('Please Input Password.')
        self.raw_password = password
        return make_password(password)

    # def clean_password2(self):
    #     password2 = self.cleaned_data['password2']
    #     if not password2:
    #         raise form.ValidationError('Please Input Password.')
    #     return password2

    # def clean(self):
    #     password = self.cleaned_data['password']
    #     password2 = self.cleaned_data['password2']
    #     if password != password2:
    #         raise form.ValidationError("Your passwords don't match.")

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Please Input Username.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Please Input Password.')
        return password

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Username or Password is incorrect 1.')
        if not user.check_password(password):
            raise forms.ValidationError('Username or Password is incorrect 2.')





