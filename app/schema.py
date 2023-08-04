import graphene
from graphene_django import DjangoObjectType
from core import models
from graphQLapi import models

class User(DjangoObjectType):
    class Meta:
        model = models.User

class CartItem(DjangoObjectType):
    class Meta:
        model = models.CartItem

class Cart(DjangoObjectType):
    class Meta:
        model = models.Cart

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int())
    cart = graphene.Field(Cart, id=graphene.Int())
    cart_items = graphene.Field(CartItem, id=graphene.Int())
    
    def resolve_cart(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return models.Cart.objects.get(pk=id)
        
        return None

schema = graphene.Schema(query=Query)