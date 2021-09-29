from django.contrib import admin
from .models import *


class AdsAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Ads, AdsAdmin)
admin.site.register(Category, CategoryAdmin)
