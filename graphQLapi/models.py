from django.db import models
from core.models import User


""""id": <<INT>>,
"itemNo": <<INT>>,
"quantity": <<INT>>,
"amount": <<INT>>
 "itemName": <<STRING>>"""

class CartItem(models.Model):
    itemName = models.CharField(max_length=100, blank=True, null=True)
    itemNo = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

class Cart(models.Model):
    cartItems = models.ForeignKey("graphQLapi.CartItem", on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)



