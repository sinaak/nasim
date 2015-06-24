from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Nasim.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/$', 'news.views.contact_us_and_news'),
    url(r'^main/womens-wear/$', 'photos.views.images'),



]
