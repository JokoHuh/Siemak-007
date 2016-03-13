from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'', include('home.urls')),
	url(r'^login/', include('home.urls')),
	#Kelembagaan
	url(r'^pt/*', include('home.urls')),
	url(r'^pts/*', include('home.urls')),
	url(r'^prod/*', include('home.urls')),
	#Kepegawaian
	url(r'^pegw/*', include('home.urls')),
	url(r'^sk/*', include('home.urls')),
	#Keakademian
	url(r'^tkrs/*', include('home.urls')),
	url(r'^mkul/*', include('home.urls')),
	url(r'^tugm/*', include('home.urls')),
	url(r'^pemb/*', include('home.urls')),
	url(r'^kelu/*', include('home.urls')),
	url(r'^khs/*', include('home.urls')),
	url(r'^ijaz/*', include('home.urls')),
	#Kemahasiswaan
	url(r'^maha/*', include('home.urls')),
	url(r'^krs/*', include('home.urls')),
	url(r'^pbay/*', include('home.urls')),

	url(r'^info/*', include('home.urls')),
]
