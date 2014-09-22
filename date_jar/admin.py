from django.contrib import admin
from date_jar.models import Category, Event


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','text',)

admin.site.register(Category)


class EventAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'description', 'url', 'location', 'image', 'address','done', 'user')

admin.site.register(Event)


