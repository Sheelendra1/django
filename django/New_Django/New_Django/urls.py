from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('app/', include('app.urls')),
    path('newapp/', include('newapp.urls')),
    path('formapp/', include('fromapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)