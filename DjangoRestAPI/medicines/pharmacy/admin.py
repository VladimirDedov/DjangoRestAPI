from django.contrib import admin

# Register your models here.
from .models import *
class AptekaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',  'price', 'is_published' )
    prepopulated_fields = {"slug": ("title",)}#С помощью этого атрибута говорим заполнять поле slug автоматически
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    fields = ('title', 'slug', 'content', 'cat', 'price', 'is_published')
    list_editable = ('is_published',)  # чтобы редактировать в админке сразу можно было

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)# , - обязательная, нужно передавать кортеж
    prepopulated_fields = {"slug":("name",)}#С помощью этого атрибута говорим заполнять поле slug автоматически на основе поля name


#Классы для регистрации в админ панеле
admin.site.register(Category, CategoryAdmin)
admin.site.register(Apteka, AptekaAdmin)

admin.site.site_title = 'Админ-панель аптеки'
admin.site.site_header = 'Админ панель Аптеки'