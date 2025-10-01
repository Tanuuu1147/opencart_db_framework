import pytest
from lib.db import create_category, create_product, get_product_by_id, delete_product, delete_category


class TestProduct:

    def test_create_category(self, connection, category_data):
    
        category_id = create_category(connection, category_data)
        assert category_id > 0
        

        delete_category(connection, category_id)

    def test_create_product(self, connection, product_data):
     
        product_id = create_product(connection, product_data)
        assert product_id > 0

        product = get_product_by_id(connection, product_id)
        assert product is not None
        assert product["model"] == product_data["model"]
        
 
        delete_product(connection, product_id)

    def test_create_product_with_fixtures(self, connection, created_product):
    
        product_id = created_product
        assert product_id > 0
        
        product = get_product_by_id(connection, product_id)
        assert product is not None

    def test_get_nonexistent_product(self, connection):
       
        product = get_product_by_id(connection, 999999)
        assert product is None




