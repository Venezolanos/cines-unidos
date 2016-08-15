from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date_of_birthday = models.DateField()
	address = models.TextField()
	phone_number = models.CharField(max_length=11)

	def __str__(self):
		return self.user.first_name