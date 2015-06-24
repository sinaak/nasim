from django.db import models



class News(models.Model):

	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'news/static/news/')

	def __str__(self):
		return self.title


class Contact(models.Model):
	name = models.CharField(max_length=100)
	phonenumber = models.CharField(max_length=20)
	email = models.EmailField(blank=True)

	def __str__(self):
		return "{}".format(self.name)

class Images(models.Model):

	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'news/static/img/')

	def __str__(self):
		return self.title















