from django.contrib import admin
from rango.models import Category, Page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}
    list_display = ('name', 'views', 'likes')

admin.site.register(Category, CatAdmin)
admin.site.register(Page, PageAdmin)