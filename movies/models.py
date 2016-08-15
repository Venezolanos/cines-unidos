from datetime import timedelta

from django.db import models

class Categorie(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Genre(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Clasification(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField(max_length=255)
	poster = models.ImageField(upload_to='static/movies/img')
	description = models.TextField()
	duration = models.DurationField(default=timedelta())
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	clasification = models.ForeignKey(Clasification, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

