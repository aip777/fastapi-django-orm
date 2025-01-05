
from django.db import models
from fapi.models.base_model import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CreateProduct(BaseModel):
    name: str
    description: str = None
    price: float = 0.0
    stock: int = 0
