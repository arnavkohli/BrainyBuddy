from django import forms
from .models import Quiz

class QuizEditForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name',)
        widgets = {
        	'name' : forms.TextInput(attrs={'placeholder':'Question Body'})
        }
        labels = {
        	'name' : False,
        }