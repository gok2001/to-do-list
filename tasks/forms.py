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
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your task',
                'rows': 4,
            }),
        }

        def clean(self):
            # cleaned_data = self.cleaned_data

            return super().clean()
