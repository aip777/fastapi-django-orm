# **FastAPI-Django-ORM**

Integrates Django ORM with FastAPI.

## **Setup**
   ```bash
   pip install -r packages.txt
   ```
---

## **Use Django commands for database migrations**

1. **Make Migrations**
   ```bash
   python manage.py makemigrations
   ```

2. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Interactive Shell**
   ```bash
   python manage.py shell
   ```

## **Development Instruction**

1. **Create a Django Project and App**
   ```bash
   django-admin startproject config .
   django-admin startapp fapi
   ```
   
2. **Update Django Settings**
   Update your `config/settings.py` with the following:

   ```python
   from pathlib import Path

   BASE_DIR = Path(__file__).resolve().parent.parent

   INSTALLED_APPS = [
       'fapi',
   ]

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
   ```

3. **Configure FastAPI to Use Django ORM**  
   Add the following at the top of your FastAPI `main.py` file:
   ```python
   import os
   import django

   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
   django.setup()
   ```

4. **Create Models and Initialize Models**
   In your `fapi/models/__init__.py` file:
   ```python
   from fapi.models.base_model import BaseModel
   from fapi.models.product import Product

   __all__ = ['BaseModel']
   __all__ += ['Product']
   ```
   
---

## **Endpoints**

- **POST `/products`**  
  Create a new product.
```bash
   [
    {
        "name": "Sample Product 1",
        "description": "First product",
        "price": 19.99,
        "stock": 50
    },
    {
        "name": "Sample Product 2",
        "description": "Second product",
        "price": 29.99,
        "stock": 30
    }
]
```

### **Products**
- **GET `/products`**  
  Fetch products from the database.
```bash
   [
    {
        "id": 1,
        "name": "New Product",
        "description": "A great new product",
        "price": "25.99",
        "stock": 100
    },
    {
        "id": 2,
        "name": "Books",
        "description": "A great new product",
        "price": "25.99",
        "stock": 100
    }
]
   ```

- **DELETE `/products/{product_id}`**  
  Delete a product by its ID.

- **DELETE `/products`**  
  Delete multiple products by providing list [1,2,3] of IDs in the request body.

## **Run the Server**

Start the FastAPI server:

```bash
fastapi dev fapi/main.py
```

Server will be accessible at `http://127.0.0.1:8000`.

---

