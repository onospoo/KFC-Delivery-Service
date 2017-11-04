from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from cart.forms import CartAddProductForm
from cart.models import Order

from main.models import Category, Product, News, ShopNumber, ShopAdress


def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_product_form = CartAddProductForm()
    return render(request, 'productlist.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form
    })

class IndexView(ListView):
    model = News
    template_name = "index.html"
    queryset = News.objects.all().order_by("-created")[:2]
    context_object_name = "news_list"

def ContactView(request):
    shop_number = ShopNumber.objects.filter(is_active=True)
    shop_adress = ShopAdress.objects.filter(is_active=True)

    return render(request, 'contacts.html', {'number_list': shop_number, 'adress_list': shop_adress})