import os
import django
from asgiref.sync import sync_to_async

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from fastapi import FastAPI
from products.models import Product
app = FastAPI()

@app.get("/products")
async def get_products():
    products = await sync_to_async(list)(Product.objects.all())
    return [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),
            "stock": product.stock,
        }
        for product in products
    ]
