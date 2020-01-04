from django.db import models
from quiz.models import Quiz, QuizAttempt
# from question.models import Question

# Create your models here.
class TorFQ(models.Model):
	quiz = models.ForeignKey(
		Quiz,
		on_delete=models.CASCADE,
	)
	body = models.CharField(max_length=255, verbose_name='Question (TorF) Body')
	is_true = models.BooleanField(verbose_name='Tick if True')
	marks = models.PositiveIntegerField()
	#img = models.ImageField(upload_to='images/', null=True, blank=True)

	@property	
	def type(self):
		return self.__class__.__name__

	@property
	def get_marks(self):
		return self.marks

#take quiz
class TorFQAttempt(models.Model):
	quiz_attempt = models.OneToOneField(
		QuizAttempt,
		on_delete=models.CASCADE
	)
	answer = models.BooleanField()
	