from django.urls import reverse, reverse_lazy  # reverse функция возвращающая нужный адресс
from django.db import models


class Apteka(models.Model):  # таблица в БД будет называться как имя класса Apteka.
    title = models.CharField(max_length=255, verbose_name="заголовок")  # title ссылка на экземпляр класса CharField
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="содержание")  # blank=True - поле может быть пустым
    price = models.CharField(max_length=255, verbose_name="Цена")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                            verbose_name="Категория")  # будет добавлено поле cat_id id - автоматически 'Category' - ссылка на модель Category

    def __str__(self):  # выводит заголовок текущей записи
        return self.title

    def get_absolute_url(self):  # функция формирования маршрута к конкретной записи
        return reverse('post', kwargs={'post_slug': self.slug})  # Маршрут с именем post по правилу из urls.py

    # функция revers стороит марщрут

    class Meta:  # Класс редактирования отображения админ панели
        verbose_name = 'Лекарства'  # чтобы в админ панеле отображалось нормальное название
        verbose_name_plural = 'Лекарства'
        ordering = ['title']  # сортировка. применяется и к самому сайту. Важное значение для пагинации


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name="Название")  # db_index=True - поле индексировано для поиска
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):  # Возвращает имя категории. Перегружен метод __str__
        return self.name

    def get_absolute_url(self):  # функция формирования маршрута к конкретной записи
        return reverse('category', kwargs={'cat_slug': self.slug})  # Маршрут с именем post по правилу из urls.py

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']
