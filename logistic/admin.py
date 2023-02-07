from django.contrib import admin

from .models import Product, Stock, StockProduct

class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 10

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    inlines = [StockProductInline, ]


# @admin.register(StockProduct)
# class StockProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'quantity', 'price',]

