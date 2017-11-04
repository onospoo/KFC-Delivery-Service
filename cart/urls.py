from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    url(r'^addl/(?P<product_id>\d+)/$', views.CartAddList, name='CartAddList'),
    url(r'^$', views.CartDetail, name='CartDetail'),
    url(r'^orders-list/$', views.OrderList, name='OrderList'),
    url(r'^orders-list/(?P<id>\d+)/$', views.OrderCheck, name='OrderCheck'),

]