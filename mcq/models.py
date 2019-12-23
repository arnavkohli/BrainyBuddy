from django.db import models
from quiz.models import Quiz

# Create your models here.
class MCQ(models.Model):
	quiz = models.ForeignKey(
		Quiz,
		on_delete=models.CASCADE,
	)
	body = models.CharField(max_length=255, verbose_name='Question (MCQ) Body')
	#img = models.ImageField(upload_to='images/', null=True, blank=True)

	@property	
	def type(self):
		return self.__class__.__name__


class MCQAnswer(models.Model):
	mcq = models.ForeignKey(
		MCQ,
		on_delete=models.CASCADE,
	)
	body = models.CharField(max_length=255, verbose_name='')
	is_correct = models.BooleanField(default=False, verbose_name='Correct')