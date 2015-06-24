from django.shortcuts import render

from news.models import News,Images

from news.forms import Contacts


def contact_us_and_news(request):
	news = News.objects.all()
	images = Images.objects.all()
	if request.method == "GET":
		form = Contacts(request.GET)
		if form.is_valid():
			form.save()
		
	else:
		form = Contacts()
	return render(request, "main.html", {
					'news': news,
					'form': form,
					'images': images,
				})