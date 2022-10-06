from django import forms
from .models import Task
from django.forms import TextInput

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields=["title","description",]
        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'style':'max-width:300px',
                'placeholder':'Task Title'
                }), 
            'description':TextInput(attrs={
                'class':'form-control',
                'style':'max-width:300px',
                'placeholder':'Description'
                })
        }