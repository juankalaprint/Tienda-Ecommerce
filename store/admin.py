from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','slug','description','price', 'stock', 'is_available', 'date_registre', 'date_update')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_available', 'date_registre', 'date_update')
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_per_page = 20
    

admin.site.register(Product, ProductAdmin)
