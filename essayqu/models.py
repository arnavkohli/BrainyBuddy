from django.db import models
from quiz.models import Quiz

# Create your models here.
class EssayQ(models.Model):
	quiz = models.ForeignKey(
		Quiz,
		on_delete=models.CASCADE,
	)
	body = models.CharField(max_length=1000, verbose_name='Question (Essay) Body')
	#img = models.ImageField(upload_to='images/', null=True, blank=True)

	@property	
	def type(self):
		return self.__class__.__name__