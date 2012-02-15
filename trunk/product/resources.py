from serenesiri.resources import BaseModelResource
from product.models import Category, Product, Price


class CategoryResource(BaseModelResource):
    model = Category


class ProductResource(BaseModelResource):
    model = Product


class PriceResource(BaseModelResource):
    model = Price