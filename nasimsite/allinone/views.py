from django.shortcuts import render

from allinone.models import New,Firstpageimage,Clothsphoto,Accesssoriesphoto,Instagramimage,Feedbacksuggestions

from allinone.forms import Contacts,Feedbacksuggestion


def contact_us_and_news(request):
	counter=False;
	news = New.objects.all()
	images = Firstpageimage.objects.all()
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
					'counter':counter,
				})





def images(request):
	counter=0;
	images = Clothsphoto.objects.all().order_by('-year')


	return render(request, "Women's-wear.html" , {
		'counter': counter,
		'images': images,

		})

def allavailable(request):

	images = Clothsphoto.objects.all().order_by('-year')


	return render(request, "All-Available.html" , {

		'images': images,

		})

def outwear(request):

	images = Clothsphoto.objects.all().order_by('-year')


	return render(request, "OutWear.html" , {
		
		'images': images,

		})
def readytowear(request):

	images = Clothsphoto.objects.all().order_by('-year')


	return render(request, "Ready-To-Wear.html" , {
		
		'images': images,

		})

def hautecouture(request):

	images = Clothsphoto.objects.all().order_by('-year')


	return render(request, "Haute-Couture.html" , {
		
		'images': images,

		})

def shawl(request):

	images = Clothsphoto.objects.all().order_by('-year')


	return render(request, "Shawl.html" , {
		
		'images': images,

		})					









def images_accessories(request):
	counter=0;
	images = Accesssoriesphoto.objects.all().order_by('-year')


	return render(request, "Accessories.html" , {
		'counter': counter,
		'images': images,

		})


def allavailable_accesssories(request):

	images = Accesssoriesphoto.objects.all().order_by('-year')


	return render(request, "allavailableaccesssories.html" , {
		
		'images': images,

		})

def necklace(request):

	images = Accesssoriesphoto.objects.all().order_by('-year')


	return render(request, "Necklace.html" , {
		
		'images': images,

		})	

def bracelet(request):

	images = Accesssoriesphoto.objects.all().order_by('-year')


	return render(request, "Bracelet.html" , {
		
		'images': images,

		})

def earring(request):

	images = Accesssoriesphoto.objects.all().order_by('-year')


	return render(request, "Earring.html" , {
		
		'images': images,

		})


def show_details(request , Clothsphoto_id):

	Clothsphoto_id = int(Clothsphoto_id)

	try:
		detail = Clothsphoto.objects.get(id=Clothsphoto_id)
	except Blog.DoesNotExist:
		raise Http404


	return render(request, "details.html" , {
		'detail' : detail,

		})


def show_details_Accessories(request , Accesssoriesphoto_id):

	Accesssoriesphoto_id = int(Accesssoriesphoto_id)

	try:
		detail = Accesssoriesphoto.objects.get(id=Accesssoriesphoto_id)
	except Blog.DoesNotExist:
		raise Http404


	return render(request, "detailsaccessories.html" , {

		'detail' : detail,

		})	



def contactus(request):
	counter=0;
	images2 = Instagramimage.objects.all()
	if request.method == "GET":
		form = Feedbacksuggestion(request.GET)
		if form.is_valid():
			form.save()
		
	else:
		form = Feedbacksuggestion()

	return render(request, "contactus.html" , {
		'counter': counter,
		'images2': images2,
		'form': form,

		})

