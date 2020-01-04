from django.db import models

from itertools import chain

from user.models import User


# Create your models here.
class Quiz(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=255)

	def get_num_questions(self):
		return len(self.mcq_set.all()) + len(self.torfq_set.all()) + len(self.essayq_set.all())

	def get_all_questions(self):
		return list(chain(self.mcq_set.all(), self.torfq_set.all(), self.essayq_set.all()))

	@property
	def get_marks(self):
		return sum([q.get_marks for q in self.get_all_questions()])
#take quiz
class QuizAttempt(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)
	quiz = models.ForeignKey(
		Quiz,
		on_delete=models.CASCADE
	)