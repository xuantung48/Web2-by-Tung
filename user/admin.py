from django.contrib import admin
from .models import CustomerUser

class CustomerAdmin(admin.ModelAdmin):
    list_filter = ['date']

admin.site.register(CustomerUser)
# Register your models here.
