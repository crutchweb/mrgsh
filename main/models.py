from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from unidecode import unidecode
from django.utils.text import slugify
import datetime
from ckeditor.fields import RichTextField


class Category(MPTTModel):
    image = models.ImageField(upload_to='category', max_length=200, blank=False, null=False, verbose_name='Изображение категории')
    name_ru = models.CharField(max_length=50, unique=True, verbose_name='Заголовок (рус)')
    description_ru = RichTextField(blank=True, null=True, verbose_name='Описание (рус)')
    name_en = models.CharField(max_length=50, unique=True, verbose_name='Заголовок (англ)')
    description_en = RichTextField(blank=True, null=True, verbose_name='Описание (англ)')
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', db_index=True, verbose_name='Родитель')
    slug = models.SlugField(max_length=50, unique=True, blank=True, verbose_name='SEO URL')

    class MPTTMeta:
        order_insertion_by = ['name_ru']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name_ru

    def get_absolute_url(self):
        return '/%s/' % self.slug

    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.name_ru))
        super(Category, self).save()


class Product(models.Model):
    image = models.ImageField(upload_to='product', max_length=200, blank=False, null=False, verbose_name='Основное Изображение продукта')
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE, verbose_name = 'Категория')
    name_ru = models.CharField(max_length=200, verbose_name='Заголовок (рус)', blank=True)
    description_ru = RichTextField(blank=True, null=True, verbose_name='Описание (рус)')
    name_en = models.CharField(max_length=200, unique=True, verbose_name='Заголовок (англ)')
    description_en = RichTextField(blank=True, null=True, verbose_name='Описание (англ)')
    slug = models.SlugField(max_length=50, unique=True, blank=True, verbose_name='SEO URL')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name_ru

    def get_absolute_url(self):
        return '/%s/' % self.slug

    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.name_ru))
        super(Product, self).save()


class News(models.Model):
    image = models.ImageField(upload_to='news', max_length=200, blank=False, null=False, verbose_name='Изображение')
    name = models.CharField(max_length=200, verbose_name='Заголовок', blank=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True, verbose_name='SEO URL')
    description = RichTextField(blank=True, null=True, verbose_name='Текст')
    created = models.DateField(default=datetime.date.today(), verbose_name='Дата')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')
    seo_keywords = models.CharField(max_length=200, verbose_name='SEO: Ключевые слова (через запятую)', blank=True)
    seo_description = models.TextField(max_length=200, verbose_name='SEO: Описание', blank=True)


    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        unique_together = ('slug', 'name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/news/%s' % self.slug

    def _get_unique_slug(self):
        slug = slugify(unidecode(self.name))
        unique_slug = slug
        num = 1
        while News.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(News, self).save()
