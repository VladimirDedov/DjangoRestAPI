from django import template
from pharmacy.models import *

register = template.Library()#через Library происходит регистрация собственных шаблонных тегов
#Простой тэг. Возвращает коолекцию данных
@register.simple_tag(name='getcats')#Декоратор связки функции с тэгом
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()#если фильтр = None
    else:
        return Category.objects.filter(pk=filter)#Возвращаем коллекцию данных


#Включающуй тег. формирует фрагмент html кода
@register.inclusion_tag('pharmacy/list_categories.html')#cats, cat_selected автоматически передается  в list_categories.html
def show_categories(sort=None, cat_selected=0):# возвращает полноценную html страницу list_categories.html
    if not sort:
        cats = Category.objects.all()  # если фильтр = None
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}#Возвращаем cats, cat_selected в list_categories.html и возвращаем
                                                        #список в базовый шаблон