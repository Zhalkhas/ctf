from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.shortcuts import get_object_or_404

class CustomUser(AbstractUser):
	score = models.IntegerField(default=0)
	class Meta:
		ordering = ('username',)
	def increase_score(self, incr):
		self.score+=incr
	def __str__(self):
		return "Username:"+str(self.username) +" score:"+ str(self.score)


class Flag(models.Model):
	flag = models.CharField(max_length=200)
	score = models.IntegerField()
	solved_users = models.ManyToManyField(CustomUser, blank=True)
	class Meta:
		ordering = ('flag',)
	def __str__(self):
		return "Flag:"+str(self.flag)
