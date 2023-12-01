from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from trensite import settings
from programm import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('programm.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = views.page_404
