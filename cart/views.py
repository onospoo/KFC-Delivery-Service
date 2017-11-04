from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from cart.models import OrderItem, Order
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm, OrderChangeStatusForm
from main.models import Product
from .tasks import OrderCreated


@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('cart:CartDetail')

@require_POST
def CartAddList(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('shop:ProductList')

def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')

def CartDetail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'update': True
            })
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         original_price=item['original_price'],
                                         quantity=item['quantity'])

            total_price = cart.get_total_price()
            if total_price < 1500: total_price += order.district.delivery_price
            cart.clear()
            send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['impylsee@gmail.com'])
            return render(request, 'ordered.html', {'order': order,'tot':total_price})

    form = OrderCreateForm()
    return render(request, 'cartp.html', {'cart': cart, 'form': form})

def OrderList(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders' : orders})

def OrderCheck(request, id):
    order = Order.objects.get(id=id)
    order_item = OrderItem.objects.filter(order_id = id)
    form = OrderChangeStatusForm(request.POST or None, instance =order)
    total_price = sum(item['price'] for item in order_item.values())
    total_original = sum(item['original_price'] for item in order_item.values())
    difference = total_price - total_original
    if form.is_valid():
        form.save()
        return redirect('cart:OrderList')
    return render(request, 'order_check.html', {'orders':order, 'form': form, 'order_item': order_item, 'total_price': total_price, 'total_original': total_original, 'difference': difference})

