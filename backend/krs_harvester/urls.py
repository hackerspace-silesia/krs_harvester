from django.conf.urls import url, include
from django.contrib import admin
from krs_harvester.routers import router

# Create your views here.
print router.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
