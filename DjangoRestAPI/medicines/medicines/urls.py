
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from medicines import settings
from django.urls import path, include
from pharmacy.views import pageNotFound



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pharmacy.urls')),#включаем урлс из приложения pharmacy - http://127.0.0.1:8000/pharmacy/

]
if settings.DEBUG:#УСЛОВИЕ ДЛЯ ДЕБАГА
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound# handler404 - специальная пременная для 404. pageNotFoud - функция обработчик