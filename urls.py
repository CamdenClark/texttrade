from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
		url(r'^listing/', include('listing.urls')),
		url(r'^admin/', admin.site.urls),
]
