from django.urls import path, include, re_path
from .views import *  #
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()  # Создан объект класса Router
router.register(r'apteka', AptekaViewSet,
                basename='apteka')  # В маршрутах имя берется по имени модели, basename - обязательно, если не указан queryset d view

urlpatterns = [  # список url patterrnsю, прописать все маршруты текущего приложения
    path('', AptekaHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),  # Динамическая ссылка
    path('category/<slug:cat_slug>/', AptekaCategory.as_view(), name='category'),
    # cat_slug передается из models.py функции get_absolut_url
    path('api/v1/drf-auth/', include('rest_framework.urls')),#маршрут для авторизации
    path('search/', search, name='search'),  # Функция представления для поиска из views.py
    path('api/v1/', include(router.urls)),  # Http://127.0.0.1:8000/api/v1/apteka
    path('api/v1/auth/', include('djoser.urls')),#Маршруты для авторизации по Токенам
    re_path(r'^auth/', include('djoser.urls.authtoken')),#Маршрут для авторизации по токенам http://127.0.0.1:8000/auth/token/login/
    # path('api/v1/aptekalist/', AptekaViewSet.as_view({'get': 'list'})),
    # path('api/v1/aptekalist/<int:pk>/', AptekaViewSet.as_view({'put': 'update'})),
]
print(urlpatterns)