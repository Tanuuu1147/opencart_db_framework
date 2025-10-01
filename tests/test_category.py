import pytest
from lib.db import create_category, create_product


def test_assign_product_to_category(connection, created_category, created_product):

    product_id = created_product
    category_id = created_category


    sql = "INSERT INTO oc_product_to_category (product_id, category_id) VALUES (%s, %s)"
    with connection.cursor() as cursor:
        cursor.execute(sql, (product_id, category_id))
    connection.commit()


    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM oc_product_to_category WHERE product_id = %s AND category_id = %s",
            (product_id, category_id)
        )
        link = cursor.fetchone()
        assert link is not None

