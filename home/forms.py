from django import forms
from .models import Todo


class TodoCreateForm(forms.Form):
    title = forms.CharField(
        max_length=150, required=False, label='Title')
    description = forms.CharField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description')
