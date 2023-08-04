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

schema = graphene.Schema(query=Query)