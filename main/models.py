from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.CharField(max_length=100,blank=True, verbose_name='Описание')
    img = models.ImageField(upload_to='product_images/', verbose_name='Картинка')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Оригинальная Цена")
    category = models.ForeignKey(Category, verbose_name="Категория")
    available = models.BooleanField(default=True, verbose_name="Доступен")

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name



class ShopAdress(models.Model):
    adress = models.CharField(max_length=300, verbose_name='Адрес')
    is_active = models.BooleanField(default=True, verbose_name="Доступен")

    class Meta:
        verbose_name = 'Адрес магазина'
        verbose_name_plural = 'Адреса магазинов'

    def __str__(self):
        return self.adress

class ShopNumber(models.Model):
    number = models.CharField(max_length=300, verbose_name='Номер телефона')
    is_active = models.BooleanField(default=True, verbose_name="Доступен")

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефона'

    def __str__(self):
        return self.number

class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.CharField(max_length=300,blank=True)
    img = models.ImageField(upload_to='news_images/', verbose_name='Картинка')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title