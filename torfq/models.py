from django.db import models
from quiz.models import Quiz

# Create your models here.
class TorFQ(models.Model):
	quiz = models.ForeignKey(
		Quiz,
		on_delete=models.CASCADE,
	)
	body = models.CharField(max_length=255, verbose_name='Question (TorF) Body')
	is_true = models.BooleanField(verbose_name='Tick if True')
	#img = models.ImageField(upload_to='images/', null=True, blank=True)

	@property	
	def type(self):
		return self.__class__.__name__