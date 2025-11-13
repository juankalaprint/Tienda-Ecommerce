from django import forms
from django.contrib import admin

from accounts import models
from .models import Category
# Register your models here.
#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_per_page = 20
    create_fields = ['name', 'slug', 'description', 'is_active']
    update_fields = ['description', 'slug', 'name', 'is_active']



    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        model = Category
        fields = ['name', 'slug', 'description', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            
        }
