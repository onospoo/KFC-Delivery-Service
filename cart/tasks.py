from celery import task
from django.conf import settings
from django.core.mail import send_mail
from .models import Order
@task
def OrderCreated(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа'.format(order.id)
    message = 'Заказ № {},\
               Имя {} \
               Способ оплаты {} \
               Время заказа {}, {}\
               Адрес ул. {}, дом {}, квартира {}, подъезд {}, этаж {} '.format(order.id, order.name, order.payment_status, order.time_order, order.date_order, order.adress, order.adress_number, order.apartment
                                                                               , order.entrance, order.floor)
    mail_send = send_mail(subject, message, settings.EMAIL_HOST_USER, ['impylsee@gmail.com'])
    return mail_send