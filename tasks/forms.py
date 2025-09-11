from django import forms
from . import models


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Task
        fields = ('title', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Name your task',
                'class': 'form-title'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your task',
                'rows': 4,
                'class': 'form-description'
            }),
        }
