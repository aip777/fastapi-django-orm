import os
import django
from asgiref.sync import sync_to_async
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from fastapi import FastAPI, HTTPException
from fapi.models.product import Product
from typing import List
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

@app.post("/products")
async def create_products(products_data: List[dict]):
    created_products = []
    for data in products_data:
        product = Product(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            stock=data["stock"],
        )
        await sync_to_async(product.save)()
        created_products.append(product)

    response = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),
            "stock": product.stock,
        }
        for product in created_products
    ]

    return response

@app.delete("/products")
async def delete_products(product_ids: list[int]):
    deleted_count, _ = await sync_to_async(Product.objects.filter(id__in=product_ids).delete)()
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return {"message": "Products have been deleted successfully."}

