from django import forms
from .models import TorFQ

class TorFQForm(forms.ModelForm):
    class Meta:
        model = TorFQ
        fields = ('body', 'is_true', )
        widgets = {
        	'body' : forms.TextInput(attrs={'placeholder':'Question Body'})
        }
        labels = {
        	'body' : False,
        }
