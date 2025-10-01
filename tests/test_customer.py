import pytest
from lib.db import (
    create_customer,
    get_customer_by_id,
    update_customer,
    delete_customer
)


class TestCustomer:

    def test_create_customer(self, connection, customer_data):
   
        customer_id = create_customer(connection, customer_data)
        assert customer_id > 0

        try:
            customer = get_customer_by_id(connection, customer_id)
            assert customer is not None
            assert customer["firstname"] == customer_data["firstname"]
            assert customer["email"] == customer_data["email"]
        finally:
            delete_customer(connection, customer_id)

    def test_update_existing_customer(self, connection, created_customer, update_data):
 
        customer_id = created_customer
        
        rows_affected = update_customer(connection, customer_id, update_data)
        assert rows_affected == 1

        updated = get_customer_by_id(connection, customer_id)
        assert updated["firstname"] == update_data["firstname"]
        assert updated["lastname"] == update_data["lastname"]
        assert updated["email"] == update_data["email"]
        assert updated["telephone"] == update_data["telephone"]

    def test_update_nonexistent_customer(self, connection, update_data):
    
        fake_id = 999999
        rows_affected = update_customer(connection, fake_id, update_data)
        assert rows_affected == 0

    def test_delete_existing_customer(self, connection, customer_data):
        
        customer_id = create_customer(connection, customer_data)
        
        rows_affected = delete_customer(connection, customer_id)
        assert rows_affected == 1

        customer = get_customer_by_id(connection, customer_id)
        assert customer is None

    def test_delete_nonexistent_customer(self, connection):

        fake_id = 999999
        rows_affected = delete_customer(connection, fake_id)
        assert rows_affected == 0

