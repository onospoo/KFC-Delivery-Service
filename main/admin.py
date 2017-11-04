from django.contrib import admin

from main.models import Category, Product, ShopAdress,ShopNumber, News


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'original_price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShopAdress)
admin.site.register(ShopNumber)
admin.site.register(News)


