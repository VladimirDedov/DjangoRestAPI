from pharmacy.models import *
from .forms import *


# Класс для выноса общего кода из view
class DataMixin:
    paginate_by = 3  # чтобы работал Пагинатор у всех классов view, наследуемых от DataMixin

    def get_user_context(self, **kwargs):  # Создает context для формирования шаблона
        context = kwargs  # формируем начальный словарь из именнованых параметров переданных get_user_context
        cats = Category.objects.all()

        context['form'] = InputForm()

        context['cats'] = cats
        if 'cat_selected' not in context:  # если в kwargs нет параметра cat_slected
            context['cat_selected'] = 0
        return context
