import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


# class AptekaModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class AptekaSerializer(serializers.Serializer):
    # class Meta:
    #     model = Apteka  # указать модель
    #     fields = ('title', 'cat_id')  # указать поля, которые передавать в API
    # title = serializers.CharField(max_length=255)  # Поля из класса AptecaModel
    # content = serializers.CharField()
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    content = serializers.CharField()
    price = serializers.CharField(max_length=10)
    is_published = serializers.BooleanField(default=True, read_only=True)#read_only - необязательное поле
    cat_id = serializers.IntegerField()

#Создание json строки
# def encode():
#     model = AptekaModel('Andjelina djoli', 'Content: Andjrlina Djoli')
#     model_sr = AptekaSerializer(model)
#     print(model_sr.data)  # .data - формируется автоматически, сериализованные данные
#     json = JSONRenderer().render(
#         model_sr.data)  # Формирование json строки. Преобразование объекта сериализации в байтовую json строку
#     print(json, type(json))
#
#
# #парсинг json строки ответа/запроса от пользователя
# def decode():
#     stream = io.BytesIO(b'{"title": "Andjelina djoli", "content":"Content: Andjrlina Djoli"}')#Байтовая строка от клиента
#     data = JSONParser().parse(stream)#Парсинг данных из потока stream
#     serializer = AptekaSerializer(data=data)#Получаем сериализированные данные. Объект сериализатора
#     serializer.is_valid()
#     print(serializer.validated_data)#Коллекция validate_data - резуьллтат декодирования json строки