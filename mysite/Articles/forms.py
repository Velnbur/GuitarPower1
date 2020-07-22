from django import forms


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
