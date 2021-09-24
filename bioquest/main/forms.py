from .models import Question
from django.forms import ModelForm, NumberInput, FileInput, Textarea, CheckboxSelectMultiple, EmailField, RadioSelect, ChoiceField

#class CheckForm(ModelForm):
 #   ANSWERS = [('а', 'а'), ('б', 'б'), ('в', 'в'), ('г', 'г')]
  #  answer = ChoiceField(widget=RadioSelect, choices=ANSWERS)


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['year', 'grade', 'stage', 'part', 'number', 'text', 'answer', 'comment', 'image', 'tags', 'Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5', 'Tag6', 'Tag7', 'Tag8', 'Tag9', 'Tag10', 'Tag11', 'imageA']
        widgets = {
            'year': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '2020',
                'type': 'number',
                'id': 'year'
            }),
            'grade': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '11',
                'type': 'number',
                'id': 'grade'
            }),
            'stage': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'ЗЭ',
                'rows': '1'
            }),
            'part': NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'placeholder': '1'
            }),
            'number': NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'placeholder': '1'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
                'rows': '8'
            }),
            'answer': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ответ',
                'rows': '1'
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
                'rows': '8'
            }),
            'image': FileInput(attrs={
                'class': 'form-control-file',
                'id': 'img',
                'type': 'file'
            }),
            'image': FileInput(attrs={
                'class': 'form-control-file',
                'id': 'imageA',
                'type': 'file'
            }),
            'tags': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),

            'Tag1': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag2': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag3': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag4': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag5': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag6': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag7': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag8': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag9': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag10': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag11': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            })
        }

class QuestionFormCont(ModelForm):
    class Meta:
        model = Question
        fields = ['year', 'grade', 'stage', 'part', 'number', 'text', 'answer', 'comment', 'image', 'tags', 'Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5', 'Tag6', 'Tag7', 'Tag8', 'Tag9', 'Tag10', 'Tag11', 'imageA']
        widgets = {
            'year': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '2020',
                'type': 'number',
                'id': 'year',
            }),
            'grade': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '11',
                'type': 'number',
                'id': 'grade'
            }),
            'stage': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'ЗЭ',
                'rows': '1'
            }),
            'part': NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'placeholder': '1'
            }),
            'number': NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'placeholder': '1'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
                'rows': '8'
            }),
            'answer': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ответ',
                'rows': '1'
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
                'rows': '8'
            }),
            'image': FileInput(attrs={
                'class': 'form-control-file',
                'id': 'img',
                'type': 'file'
            }),
            'image': FileInput(attrs={
                'class': 'form-control-file',
                'id': 'imageA',
                'type': 'file'
            }),
            'tags': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag1': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag2': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag3': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag4': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag5': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag6': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag7': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag8': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag9': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag10': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            }),
            'Tag11': CheckboxSelectMultiple(attrs={
                'type': 'checkbox'
            })
        }



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text=' Используйте реальный адрес электронной почты.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


