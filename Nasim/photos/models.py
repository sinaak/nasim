from django.db import models



class Availablenow(models.Model):
	
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	image = models.ImageField(upload_to = 'news/static/images/availablenow')

	def __str__(self):
		return self.title



