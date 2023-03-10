import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


# class AptekaModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class AptekaSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)#Создается скрытое поле с прописанным полем user
    class Meta:
        model=Apteka
        fields = ('id','title', 'slug', 'content', 'price', 'cat', 'user')






#Добавление данных в БД только с классом Serializer
#     def create(self, validated_data):#Медот добавления данных в БД, запускается при валидации данных
#         return Apteka.objects.create(**validated_data)
#
# #Изменение данных записи в БД
#     def update(self, instance, validated_data):#instance - объект модели Apteka
#         instance.title = validated_data.get('title', instance)
#         instance.slug = validated_data.get('slug', instance)
#         instance.content = validated_data.get('content', instance)
#         instance.price = validated_data.get('price', instance)
#         instance.is_published = validated_data.get('is_publisher', instance)
#         instance.cat_id = validated_data.get('cat_id', instance)
#         return instance
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