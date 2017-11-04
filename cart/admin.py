from django.contrib import admin

from cart.models import OrderItem, Order, Couriers, District


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'order_status', 'created', 'updated']
    list_filter = ['order_status', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Couriers)
admin.site.register(District)