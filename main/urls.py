from django.conf.urls import url

from main.views import IndexView
from . import views

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^shop/(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^shop/$', views.ProductList, name='ProductList'),
    url(r'^contacts/$', views.ContactView, name='ContactsList'),
]