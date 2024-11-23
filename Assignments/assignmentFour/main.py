import requests
import json
from tabulate import tabulate


# Function that sends an HTTP GET request to retrieve the clothes_shop data from the
# stock-list endpoint.
def get_stock_list_fe():
    result = requests.get(
        'http://127.0.0.1:5001/stock-list')
    return result.json()


# Function that sends an HTTP DELETE request to the discontinued endpoint, to delete the item
# with the ID number input.
def delete_item_fe(user_input_id):
    result = requests.delete(
        f'http://127.0.0.1:5001/discontinued/{user_input_id}')
    return result.json()


# Function that sends an HTTP POST request to the new-stock endpoint, to add an item
# with item type and stock number input (both assigned to keys in a dictionary).
def add_item_fe(user_input_item_type, user_input_stock_number):
    item_details = {
        "new_stock_type": user_input_item_type,
        "new_stock_level": int(user_input_stock_number)
    }
    result = requests.post(
        'http://127.0.0.1:5001/new-stock',
        headers={'content-type': 'application/json'},
        data=json.dumps(item_details)
    )
    return result.json()


# Function that sends an HTTP PUT request to the updated-stock endpoint, to update the item
# with the ID number and stock level input (both assigned to keys in a dictionary).
def update_stock_fe(user_input_id, user_input_stock_number):
    item_details = {
        "item_id_to_change": int(user_input_id),
        "stock_level_to_change": int(user_input_stock_number)
    }
    result = requests.put(
        'http://127.0.0.1:5001/updated-stock',
        headers={'content-type': 'application/json'},
        data=json.dumps(item_details)
    )
    return result.json()


# This function from the imported module tabulate presents the list data from the SQL query
# in the form of a table with headings that correspond to the schema, so that the stock information
# is more readable for the user.
def tabulate_stock_data(data):
    tabulated_data = tabulate(data, headers=["Item ID", "Item Type", "Number In Stock"])
    return tabulated_data


# Function to ensure the ID input relates to an actual item in the table.
def get_all_str_item_ids(sql_stock_list_data):
    all_item_ids = [str(item[0]) for item in sql_stock_list_data]
    return all_item_ids


# This function runs our Stock Room program.
def run():
    print('---------------------------------------------------------')
    print('This is your Stock Room. What would you like to do?')
    print('---------------------------------------------------------')
    print("A: View full stock-list")
    print("B: Update stock levels")
    print("C: Remove an item")
    print("D: Add new item")
    print('----------------------------------------------------------')
    answer = input("Choose an option (A-D) from the above. ").strip().upper()
    print()
    sql_stock_list = get_stock_list_fe()
    stock_list = tabulate_stock_data(sql_stock_list)

    if answer == "A":
        print("Here is the current stock-list: \n")
        print(stock_list)
        print("\nIf you would like to make more changes, please re-run the program.")
        return

    elif answer == "B":
        print("Here is the current stock-list: \n")
        print(stock_list)
        id_to_update = input("\nEnter the ID of the item you would like to update: ").strip()
        while id_to_update not in get_all_str_item_ids(sql_stock_list):
            id_to_update = input("\nEnter the ID of the item you would like to update: ").strip()
        stock_number_to_update = input("\nEnter the new stock amount (as a whole integer): ").strip()
        update_stock_fe(id_to_update, stock_number_to_update)
        print(f"\nItem {id_to_update} updated.")

    elif answer == "C":
        print("Here is the current stock-list: \n")
        print(stock_list)
        id_to_remove = input("\nEnter the ID of the item you would like to remove: ").strip()
        while id_to_remove not in get_all_str_item_ids(sql_stock_list):
            id_to_remove = input("\nEnter the ID of the item you would like to remove: ").strip()
        delete_item_fe(id_to_remove)
        print(f"\nItem {id_to_remove} discontinued.")

    elif answer == "D":
        new_item = input("Enter the type of item you would like to add: ").strip().capitalize()
        new_stock_number = input("\nEnter the stock amount for the new item (as a whole integer): ").strip()
        add_item_fe(new_item, new_stock_number)
        print("\nItem added.")

    else:
        print("Invalid option. Please re-run and select an option A-D.")
        return

    updated_stock_list = get_stock_list_fe()
    print("\nHere is the updated stock-list: \n")
    print(tabulate_stock_data(updated_stock_list))
    print("\nIf you would like to make more changes, please re-run the program.")


# Ensures the Stock Room program runs when the file is run, but not when it is imported.
if __name__ == '__main__':
    run()
