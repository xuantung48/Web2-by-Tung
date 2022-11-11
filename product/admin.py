from django.contrib import admin
from .models import Category, Product, Variation
class productAdmin(admin.ModelAdmin):
    list_filter = ['date']
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variation)
# Register your models here.
