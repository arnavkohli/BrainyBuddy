from django.db import models
from quiz.models import Quiz, QuizAttempt
# from question.models import Question

# Create your models here.
class MCQ(models.Model):
	quiz = models.ForeignKey(
		Quiz,
		on_delete=models.CASCADE,
	)
	body = models.CharField(max_length=255, verbose_name='Question (MCQ) Body')
	marks = models.PositiveIntegerField()
	#img = models.ImageField(upload_to='images/', null=True, blank=True)

	@property	
	def type(self):
		return self.__class__.__name__

	@property
	def get_marks(self):
		return self.marks

	def get_answers_list(self):
		return MCQAnswer.objects.filter(mcq__exact=self)
	


class MCQAnswer(models.Model):
	mcq = models.ForeignKey(
		MCQ,
		on_delete=models.CASCADE,
	)
	body = models.CharField(max_length=255, verbose_name='')
	is_correct = models.BooleanField(default=False, verbose_name='Correct')

# take quiz
class MCQAttempt(models.Model):
	quiz_attempt = models.OneToOneField(
		QuizAttempt,
		on_delete=models.CASCADE
	)
	mcq = models.ForeignKey(
		MCQ,
		on_delete=models.CASCADE
	)