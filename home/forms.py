from django import forms


class TodoCreateForm(forms.Form):
    title = forms.CharField(
        max_length=150, required=False, label='Title')
    description = forms.CharField()
