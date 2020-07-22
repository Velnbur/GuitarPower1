from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'Search',
            'autocomplete': 'off'
        }),
        error_messages={}
    )
