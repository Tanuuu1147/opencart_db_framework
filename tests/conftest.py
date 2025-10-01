import pytest
import uuid
import time
from lib.db import (
    create_customer,
    delete_customer,
    create_category,
    delete_category,
    create_product,
    delete_product
)


@pytest.fixture
def customer_data():
   
    unique_id = str(uuid.uuid4())[:8]
    return {
        "customer_group_id": 1,
        "store_id": 0,
        "language_id": 1,
        "firstname": f"John_{unique_id}",
        "lastname": f"Doe_{unique_id}",
        "email": f"john.doe.{unique_id}@example.com",
        "telephone": f"123456{unique_id[:4]}",
        "password": "hashed_password",
        "salt": "abc123",
        "cart": None,
        "wishlist": None,
        "newsletter": 0,
        "address_id": 0,
        "ip": "127.0.0.1",
        "status": 1,
        "approved": 1,
        "token": "",
        "code": "",
        "date_added": time.strftime('%Y-%m-%d %H:%M:%S')
    }


@pytest.fixture
def update_data():

    unique_id = str(uuid.uuid4())[:8]
    return {
        "firstname": f"Jane_{unique_id}",
        "lastname": f"Smith_{unique_id}",
        "email": f"jane.smith.{unique_id}@example.com",
        "telephone": f"987654{unique_id[:4]}"
    }


@pytest.fixture
def created_customer(connection, customer_data):

    customer_id = create_customer(connection, customer_data)
    yield customer_id
    try:
        delete_customer(connection, customer_id)
    except Exception:
        pass  


@pytest.fixture
def category_data():
  
    unique_id = str(uuid.uuid4())[:6]
    return {
        "image": "",
        "parent_id": 0,
        "top": 1,
        "column": 1,
        "sort_order": 1,
        "status": 1,
        "language_id": 1,
        "name": f"Category_{unique_id}",
        "description": f"Description for category {unique_id}",
        "meta_title": f"Meta {unique_id}",
        "meta_description": "",
        "meta_keyword": ""
    }


@pytest.fixture
def created_category(connection, category_data):
  
    category_id = create_category(connection, category_data)
    yield category_id
    try:
        delete_category(connection, category_id)
    except Exception:
        pass  


@pytest.fixture
def product_data():
 
    unique_id = str(uuid.uuid4())[:6]
    return {
        "model": f"Model_{unique_id}",
        "sku": f"SKU-{unique_id}",
        "upc": "",
        "ean": "",
        "jan": "",
        "isbn": "",
        "mpn": "",
        "location": "Warehouse",
        "quantity": 10,
        "stock_status_id": 7,
        "image": "",
        "manufacturer_id": 0,
        "shipping": 1,
        "price": 99.99,
        "points": 0,
        "tax_class_id": 0,
        "weight": 0.5,
        "weight_class_id": 1,
        "length": 10,
        "width": 5,
        "height": 2,
        "length_class_id": 1,
        "subtract": 1,
        "minimum": 1,
        "sort_order": 0,
        "status": 1,
        "language_id": 1,
        "name": f"Product {unique_id}",
        "description": f"Description for product {unique_id}",
        "tag": "test",
        "meta_title": f"Product {unique_id}",
        "meta_description": "",
        "meta_keyword": "test"
    }


@pytest.fixture
def created_product(connection, product_data):

    product_id = create_product(connection, product_data)
    yield product_id
    try:
        delete_product(connection, product_id)
    except Exception:
        pass 
