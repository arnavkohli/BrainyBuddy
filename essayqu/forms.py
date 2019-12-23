from django import forms
from .models import EssayQ

class EssayQForm(forms.ModelForm):
    class Meta:
        model = EssayQ
        fields = ('body', )
        widgets = {
        	'body' : forms.Textarea()
        }
        labels = {
        	'body' : False,
        }