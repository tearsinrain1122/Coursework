from flask import Flask, jsonify, request
from db_utils import get_all_stock_levels, delete_item_by_id, add_new_item, update_stock_number_by_id

app = Flask(__name__)


# Flask route for GET requests
@app.route('/stock-list', methods=['GET'])
def get_stock_list():
    return jsonify(get_all_stock_levels())


# Flask route for DELETE requests
@app.route('/discontinued/<int:user_input_id>', methods=['DELETE'])
def delete_stock_lines(user_input_id):
    return jsonify(delete_item_by_id(user_input_id))


# Flask route for POST requests
@app.route('/new-stock', methods=['POST'])
def new_stock_line():
    new_item = request.get_json()
    return jsonify(add_new_item(new_item["new_stock_type"], new_item["new_stock_level"]))


# Flask route for PUT requests
@app.route('/updated-stock', methods=['PUT'])
def update_stock_level():
    new_stock_details = request.get_json()
    return jsonify(update_stock_number_by_id(new_stock_details["item_id_to_change"],
                                             new_stock_details["stock_level_to_change"]))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
