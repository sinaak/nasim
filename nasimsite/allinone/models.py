from django.db import models


class Clothsphoto(models.Model):

	title = models.CharField(max_length=100)
	description = models.TextField(max_length=300)
	image = models.ImageField(upload_to = 'images/cloths')
	Model = models.IntegerField(choices=((1, ("OutWear")),
                                        (2, ("Ready To Wear ")),
                                        (3, ("Haute Couture")),
                                        (4, ("Shawl")),
                                        (5, ("Others"))),
                                default=1)
	is_available = models.BooleanField()
	year = models.DateTimeField()
	Fasl = models.IntegerField(choices=((1, ("paeez")),
                                        (2, ("zemestoon")),
                                        (3, ("tabestoon")),
                                        (4, ("bahar"))),
                                default=1)
	
	def __str__(self):
		return self.title



class Accesssoriesphoto(models.Model):

	title = models.CharField(max_length=100)
	description = models.TextField(max_length=300)
	image = models.ImageField(upload_to = 'images/accesssories')
	Model = models.IntegerField(choices=((1, ("Necklace")),
                                        (2, ("Bracelet ")),
                                        (3, ("Earring")),
                                        (4, ("Others"))),
                                default=1)
	is_available = models.BooleanField()
	year = models.DateTimeField()

	def __str__(self):
		return self.title

class New(models.Model):

	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'images/news')
	def __str__(self):
		return self.title


class Contact(models.Model):
	name = models.CharField(max_length=100)
	phonenumber = models.CharField(max_length=20)
	email = models.EmailField(blank=True)

	def __str__(self):
		return "{}".format(self.name)

class Feedbacksuggestions(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	comment = models.CharField(max_length=20)
	
	def __str__(self):
		return "{}".format(self.name)

class Firstpageimage(models.Model):

	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'images/firstpageslideshow/')

	def __str__(self):
		return self.title


class Instagramimage(models.Model):

	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'images/instagramimages/')

	def __str__(self):
		return self.title		
