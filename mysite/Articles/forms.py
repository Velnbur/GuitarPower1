from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from .models import ArticleModel


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
