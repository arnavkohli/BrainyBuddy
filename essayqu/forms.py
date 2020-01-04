from django import forms
from .models import EssayQ, EssayQAttempt

class EssayQForm(forms.ModelForm):
    class Meta:
        model = EssayQ
        fields = ('body', 'marks',)
        widgets = {
        	'body' : forms.Textarea()
        }
        # labels = {
        # 	'body' : False,
        # }
class EssayQAttemptForm(forms.ModelForm):
	class Meta:
		model = EssayQAttempt
		fields = ('answer',)