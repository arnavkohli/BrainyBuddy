from django import forms
from .models import EssayQ

class EssayQForm(forms.ModelForm):
    class Meta:
        model = EssayQ
        fields = ('body', 'answer', )
        widgets = {
        	'body' : forms.TextInput(attrs={'placeholder':'Question Body'})
        }
        labels = {
        	'body' : False,
        }