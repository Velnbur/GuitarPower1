from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'forums-input',
            'placeholder': 'Search',
            'autocomplete': 'off'
        }),
        error_messages={}
    )


class FilterForm(forms.Form):
    FILTER = (
        ('from_new_to_old', 'From new to old'),
        ('from_old_to_new', 'From old to new'),
        ('most_popular', 'Most popular')
    )
    order_choices = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={
                'class': '',

            }
        ),
        choices=FILTER,
    )

    pub_date_from = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            }
        )
    )
    pub_date_to = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            }
        )
    )
