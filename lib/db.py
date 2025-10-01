import pymysql
import time


def create_customer(connection, customer_data):

    sql = """
    INSERT INTO oc_customer (
        customer_group_id, store_id, language_id, firstname, lastname, 
        email, telephone, password, salt, cart, wishlist, newsletter, 
        address_id, ip, status, approved, token, code, date_added
    ) VALUES (
        %(customer_group_id)s, %(store_id)s, %(language_id)s, %(firstname)s, %(lastname)s,
        %(email)s, %(telephone)s, %(password)s, %(salt)s, %(cart)s, %(wishlist)s, %(newsletter)s,
        %(address_id)s, %(ip)s, %(status)s, %(approved)s, %(token)s, %(code)s, %(date_added)s
    )
    """
    
    with connection.cursor() as cursor:
        cursor.execute(sql, customer_data)
        customer_id = cursor.lastrowid
    connection.commit()
    return customer_id


def get_customer_by_id(connection, customer_id):

    sql = "SELECT * FROM oc_customer WHERE customer_id = %s"
    
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()


def update_customer(connection, customer_id, update_data):
  
    set_clauses = []
    values = []
    
    for key, value in update_data.items():
        set_clauses.append(f"{key} = %s")
        values.append(value)
    
    values.append(customer_id)  
    
    sql = f"UPDATE oc_customer SET {', '.join(set_clauses)} WHERE customer_id = %s"
    
    with connection.cursor() as cursor:
        rows_affected = cursor.execute(sql, values)
    connection.commit()
    return rows_affected


def delete_customer(connection, customer_id):
 
    sql = "DELETE FROM oc_customer WHERE customer_id = %s"
    
    with connection.cursor() as cursor:
        rows_affected = cursor.execute(sql, (customer_id,))
    connection.commit()
    return rows_affected


def create_category(connection, category_data):
 

    category_sql = """
    INSERT INTO oc_category (
        image, parent_id, top, `column`, sort_order, status, date_added, date_modified
    ) VALUES (
        %(image)s, %(parent_id)s, %(top)s, %(column)s, %(sort_order)s, %(status)s, NOW(), NOW()
    )
    """
    
    with connection.cursor() as cursor:
        cursor.execute(category_sql, category_data)
        category_id = cursor.lastrowid
        
      
        description_sql = """
        INSERT INTO oc_category_description (
            category_id, language_id, name, description, meta_title, meta_description, meta_keyword
        ) VALUES (
            %s, %(language_id)s, %(name)s, %(description)s, %(meta_title)s, %(meta_description)s, %(meta_keyword)s
        )
        """
        
        description_data = {
            'language_id': category_data['language_id'],
            'name': category_data['name'],
            'description': category_data['description'],
            'meta_title': category_data['meta_title'],
            'meta_description': category_data['meta_description'],
            'meta_keyword': category_data['meta_keyword']
        }
        
        cursor.execute(description_sql, (category_id, *description_data.values()))
    
    connection.commit()
    return category_id


def delete_category(connection, category_id):
  
    with connection.cursor() as cursor:
       
        cursor.execute("DELETE FROM oc_category_description WHERE category_id = %s", (category_id,))
        
   
        rows_affected = cursor.execute("DELETE FROM oc_category WHERE category_id = %s", (category_id,))
    
    connection.commit()
    return rows_affected


def create_product(connection, product_data):
   
   
    product_sql = """
    INSERT INTO oc_product (
        model, sku, upc, ean, jan, isbn, mpn, location, quantity, stock_status_id,
        image, manufacturer_id, shipping, price, points, tax_class_id, date_available,
        weight, weight_class_id, length, width, height, length_class_id,
        subtract, minimum, sort_order, status, date_added, date_modified
    ) VALUES (
        %(model)s, %(sku)s, %(upc)s, %(ean)s, %(jan)s, %(isbn)s, %(mpn)s, %(location)s,
        %(quantity)s, %(stock_status_id)s, %(image)s, %(manufacturer_id)s, %(shipping)s,
        %(price)s, %(points)s, %(tax_class_id)s, NOW(), %(weight)s, %(weight_class_id)s,
        %(length)s, %(width)s, %(height)s, %(length_class_id)s, %(subtract)s,
        %(minimum)s, %(sort_order)s, %(status)s, NOW(), NOW()
    )
    """
    
    with connection.cursor() as cursor:
        cursor.execute(product_sql, product_data)
        product_id = cursor.lastrowid
        
    
        description_sql = """
        INSERT INTO oc_product_description (
            product_id, language_id, name, description, tag, meta_title, meta_description, meta_keyword
        ) VALUES (
            %s, %(language_id)s, %(name)s, %(description)s, %(tag)s, %(meta_title)s, %(meta_description)s, %(meta_keyword)s
        )
        """
        
        description_data = {
            'language_id': product_data['language_id'],
            'name': product_data['name'],
            'description': product_data['description'],
            'tag': product_data['tag'],
            'meta_title': product_data['meta_title'],
            'meta_description': product_data['meta_description'],
            'meta_keyword': product_data['meta_keyword']
        }
        
        cursor.execute(description_sql, (product_id, *description_data.values()))
    
    connection.commit()
    return product_id


def get_product_by_id(connection, product_id):

    sql = """
    SELECT p.*, pd.name, pd.description 
    FROM oc_product p 
    LEFT JOIN oc_product_description pd ON p.product_id = pd.product_id 
    WHERE p.product_id = %s AND pd.language_id = 1
    """
    
    with connection.cursor() as cursor:
        cursor.execute(sql, (product_id,))
        return cursor.fetchone()


def delete_product(connection, product_id):
    
    with connection.cursor() as cursor:

        cursor.execute("DELETE FROM oc_product_description WHERE product_id = %s", (product_id,))
        
       
        cursor.execute("DELETE FROM oc_product_to_category WHERE product_id = %s", (product_id,))
        
 
        rows_affected = cursor.execute("DELETE FROM oc_product WHERE product_id = %s", (product_id,))
    
    connection.commit()
    return rows_affected