import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


# Defining a class to raise a custom exception error in the below functions when connection to the database
# is not possible.
class DbConnectionError(Exception):
    pass


# Connecting to the database clothes_shop, using credentials imported from config.py file
# (Please ensure HOST, USER and PASSWORD details are filled in)
def db_connection_setup():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx


# This function connects to the clothes_shop database, and runs a query that selects all the data
# from the table stock_room. As in each of the functions below, a connection error is raised
# if connection to the database is not successful.
def get_all_stock_levels():
    db_connection = None
    try:
        db_connection = db_connection_setup()
        db_cursor = db_connection.cursor()
        print(f"Successfully connected to: {DATABASE}.")

        query = "SELECT * FROM stock_room"

        db_cursor.execute(query)
        all_stock_list_data = db_cursor.fetchall()
        db_cursor.close()
        return all_stock_list_data

    except Exception:
        raise DbConnectionError(f"Failed to access {DATABASE}, please troubleshoot and try again.")

    finally:
        if db_connection:
            db_connection.close()
            print(f"Disconnected from: {DATABASE}.")


# This function runs a query in the clothes_shop database that deletes an item from the
# stock_room table according to the ID that is input when called.
def delete_item_by_id(input_id):
    db_connection = None
    try:
        db_connection = db_connection_setup()
        db_cursor = db_connection.cursor()
        print(f"Successfully connected to: {DATABASE}.")

        query = f"""DELETE FROM stock_room 
        WHERE item_id = {input_id}"""

        db_cursor.execute(query)
        db_connection.commit()
        db_cursor.close()
        return f"Item {input_id} discontinued."

    except Exception:
        raise DbConnectionError(f"Failed to access {DATABASE}, please troubleshoot and try again.")

    finally:
        if db_connection:
            db_connection.close()
            print(f"Disconnected from: {DATABASE}.")


# This function runs a query in the clothes_shop database that adds a new item to the stock_room table when called. 
# The function has two arguments which correspond to the schema in the stock_room table (the item_id
# in the stock_room table is auto-increment, so does not require manual input).
def add_new_item(input_item_type, input_stock_number):
    db_connection = None
    try:
        db_connection = db_connection_setup()
        db_cursor = db_connection.cursor()
        print(f"Successfully connected to: {DATABASE}.")
        item_to_add = [input_item_type, input_stock_number]

        query = """INSERT INTO stock_room 
        (item_type, number_in_stock) 
        VALUES (%s, %s)"""

        db_cursor.execute(query, item_to_add)
        db_connection.commit()
        db_cursor.close()
        return f"Item added."

    except Exception:
        raise DbConnectionError(f"Failed to access {DATABASE}, please troubleshoot and try again.")

    finally:
        if db_connection:
            db_connection.close()
            print(f"Disconnected from: {DATABASE}.")


# This function runs a query in the clothes_shop database that updates an item from the
# stock_room table according to the ID and new stock number that are input when called.
def update_stock_number_by_id(input_id, input_stock_number):
    db_connection = None
    try:
        db_connection = db_connection_setup()
        db_cursor = db_connection.cursor()
        print(f"Successfully connected to: {DATABASE}.")

        query = f"""UPDATE stock_room
        SET 
        number_in_stock = {input_stock_number}
        WHERE
        item_id = {input_id}
        """

        db_cursor.execute(query)
        db_connection.commit()
        db_cursor.close()
        return f"Item {input_id} updated."

    except Exception:
        raise DbConnectionError(f"Failed to access {DATABASE}, please troubleshoot and try again.")

    finally:
        if db_connection:
            db_connection.close()
            print(f"Disconnected from: {DATABASE}.")
