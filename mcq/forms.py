from django import forms
from .models import MCQ, MCQAnswer

class MCQForm(forms.ModelForm):
    class Meta:
        model = MCQ
        fields = ('body', 'marks')
        widgets = {
        	'body' : forms.TextInput(attrs={'placeholder':'Question Body'})
        }
        labels = {
        	'body' : False,
        }

class MCQAnswerForm(forms.ModelForm):
	class Meta:
		model = MCQAnswer
		fields = ('body', 'is_correct',)
