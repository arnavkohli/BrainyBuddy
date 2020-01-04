from django import forms
from .models import MCQ, MCQAnswer, MCQAttempt
# from question.models import Question
from django.forms.widgets import RadioSelect

class MCQForm(forms.ModelForm):
    class Meta:
        model = MCQ
        fields = ('body', 'marks',)
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

class MCQQAttemptForm(forms.ModelForm):
    class Meta:
        model = MCQAttempt
        exclude = ('quiz_attempt', 'mcq',)
    def __init__(self, question, *args, **kwargs):
        super(MCQQAttemptForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)

