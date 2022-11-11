from django.db import models
from user.models import CustomerUser
from catalog.models import Cart
# Create your models here.
class Order (models.Model):
    user = models.ForeignKey(CustomerUser, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    shipping = models.CharField(default = '', max_length = 150)
    order_description = models.TextField(default = '')
    is_complete = models.BooleanField (default = False)