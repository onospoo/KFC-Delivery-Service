from django.db import models
from django.urls import reverse

from main.models import Product

PAYMENT_STATUS_CHOICES = {
    ('Карта', 'Cбербанк ОНЛАЙН'),
    ('Нал', 'Наличные'),
}

ORDER_STATUS_CHOICES = {
    ('Новый', 'Новый'),
    ('Выполняется', 'Выполняется'),
    ('Завершен', 'Завершен'),
}

class District(models.Model):
    name = models.CharField(verbose_name='Имя района', max_length=100)
    delivery_price = models.DecimalField(verbose_name='Цена доставки', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name + "(" + str(self.delivery_price) + ")"


class Couriers(models.Model):
    name = models.CharField(verbose_name='Имя курьера', max_length=100)

    class Meta:
        verbose_name = "Курьер"
        verbose_name_plural = 'Курьеры'

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    number = models.CharField(verbose_name='Номер телефона', max_length=20)
    district = models.ForeignKey(District, verbose_name='Район')
    adress = models.CharField(verbose_name='Улица', max_length=30)
    adress_number = models.CharField(verbose_name='Номер дома', max_length=10)
    apartment = models.CharField(verbose_name='Квартира', blank = True, max_length=10, null=True)
    entrance = models.PositiveIntegerField(verbose_name='Подъезд', blank=True, null=True)
    floor = models.PositiveIntegerField(verbose_name='Этаж', blank=True, null=True)
    order_status = models.CharField(max_length=20, verbose_name='Состояние заказа', choices=ORDER_STATUS_CHOICES, default='Новый')
    payment_status = models.CharField(verbose_name='Способ оплаты', max_length=30, choices=PAYMENT_STATUS_CHOICES, default='Нал')
    courier = models.ForeignKey(Couriers, verbose_name='Курьер', default=1)
    time_order = models.CharField(verbose_name='Время заказа', blank=True, max_length=5)
    date_order = models.CharField(verbose_name='Дата заказа', blank=True, max_length=15)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_absolute_url(self):
        return reverse('cart:OrderCheck', args=[self.id])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    original_price = models.DecimalField(verbose_name='Оригинальная цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity