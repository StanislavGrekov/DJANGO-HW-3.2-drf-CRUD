from django.core.management.base import BaseCommand
from logistic.models import Product, Stock, StockProduct



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        # products = Product.objects.all()
        # print(products)
        stocks = Stock.objects.all()
        for stock in stocks:
            print(stock)
            for elements in stock.positions.all():
                print(elements.product.title)
                print(elements.quantity)
                print(elements.price)

        # product1=Product.objects.create(title = 'Макарошки', description='Свежий макарошек')
        # stock1 =Stock.objects.create(address = 'Луночарского 2')
        # stockproduct = StockProduct.objects.create(stock =stock1, product=product1, quantity=2, price=17.2)

