from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from main.models import *
from django.utils.html import format_html


def get_picture_preview(obj):
    if obj.pk:
        return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;" />'.format(obj.image.url))
    return "(Выберите изображение и сохраните, чтобы увидеть превью)"
get_picture_preview.allow_tags = True


class CategoryAdmin(DjangoMpttAdmin):

    def image_img(self, obj):
        return format_html('<img src="{}" width="50px"/>'.format(obj.image.url))

    list_display = ('name_ru',)
    fields = [get_picture_preview, 'image', 'name_ru', 'description_ru', 'name_en', 'description_en', 'parent', 'slug']
    readonly_fields = [get_picture_preview]	
    list_per_page = 10


class ProductAdmin(admin.ModelAdmin):

    def image_img(self, obj):
        return format_html('<img src="{}" width="50px"/>'.format(obj.image.url))

    list_display = ('name_ru',)
    fields = [get_picture_preview, 'image', 'category', 'name_ru', 'description_ru', 'name_en', 'description_en', 'slug']
    readonly_fields = [get_picture_preview] 
    list_per_page = 10


class NewsAdmin(admin.ModelAdmin):

    def image_img(self, obj):
        return format_html('<img src="{}" width="50px"/>'.format(obj.image.url))

    list_display = ('name', 'slug', 'created', 'published',)
    fields = [get_picture_preview, 'image', 'name', 'slug', 'description', 'created', 'published', 'seo_keywords', 'seo_description']	
    readonly_fields = [get_picture_preview] 
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(News, NewsAdmin)