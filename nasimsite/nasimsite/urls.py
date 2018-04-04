from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'nasimsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'allinone.views.contact_us_and_news'),
    url(r'^contact/$', 'allinone.views.contactus'),
    url(r'^womens-wear/$', 'allinone.views.images'),
    url(r'^womens-wear/allavailable$', 'allinone.views.allavailable'),
    url(r'^womens-wear/outwear$', 'allinone.views.outwear'),
    url(r'^womens-wear/readytowear$', 'allinone.views.readytowear'),
    url(r'^womens-wear/hautecouture$', 'allinone.views.hautecouture'),
    url(r'^womens-wear/shawl$', 'allinone.views.shawl'),


    url(r'^accessories/$', 'allinone.views.images_accessories'),
    url(r'^accessories/allavailable$', 'allinone.views.allavailable_accesssories'),
    url(r'^accessories/necklace$', 'allinone.views.necklace'),
    url(r'^accessories/bracelet$', 'allinone.views.bracelet'),
    url(r'^accessories/earring$', 'allinone.views.earring'),


    url(r'^womens-wear/clothphoto/(?P<Clothsphoto_id>\d+)/$', 'allinone.views.show_details'),
    url(r'^accessories/accessoriesphoto/(?P<Accesssoriesphoto_id>\d+)/$', 'allinone.views.show_details_Accessories'),




] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)