from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from .models import ArticleModel, CommentModel, CommentAnswerModel


class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'forums-input',
            'placeholder': 'Search Posts',
            'autocomplete': 'off',
            'onfocus': 'this.placeholder=""',
            'onblur': 'this.placeholder="Search Posts"'
        }),
        error_messages={}
    )


class ArticleForm(ModelForm):
    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = ArticleModel
        fields = ['text', 'heading', 'image']


class CommentForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': '',
                                                        'placeholder': '',
                                                        }))

    class Meta:
        model = CommentModel
        fields = ['text']


class CommentAnswerForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': '',
                                                        'placeholder': '',
                                                        }))

    class Meta:
        model = CommentAnswerModel
        fields = ['text']
