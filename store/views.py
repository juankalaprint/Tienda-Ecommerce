from django.shortcuts import render
from .models import Product
# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)
    counter_products = products.count()
    context ={
        "products" : products,
        "counter_products": counter_products,
        
    }
    return render(request, "store/tienda.html",context=context)