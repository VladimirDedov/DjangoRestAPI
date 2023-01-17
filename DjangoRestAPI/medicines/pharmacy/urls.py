from django.urls import path
from .views import *#
from .views import *
urlpatterns = [# список url patterrnsю, прописать все маршруты текущего приложения
    path('', AptekaHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),#Динамическая ссылка
    path('category/<slug:cat_slug>/', AptekaCategory.as_view(), name='category'),#cat_slug передается из models.py функции get_absolut_url
    path('search/', search, name='search'),#Функция представления для поиска из views.py
    path('api/v1/aptekalist/', AptekaAPIList.as_view()),
    path('api/v1/aptekalist/<int:pk>/', AptekaAPIUpdate.as_view()),
    path('api/v1/aptekadetail/<int:pk>/', AptekaAPIDetailView.as_view())
]