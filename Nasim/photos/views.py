from django.shortcuts import render

from photos.models import Availablenow


def images(request):
	counter=0;
	images = Availablenow.objects.all()


	return render(request, "Women's-wear.html" , {
		'counter': counter,
		'images': images,

		})