import uuid

from flask import Flask, request
from flask_smorest import abort

from db import items

app = Flask(__name__)


@app.get('/item')
def get_all_items():
    return {'items': list(items.values())}


@app.get('/item/<string:item_id>')
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message='Item not found.')


@app.post('/item')
def create_item():
    item_data = request.get_json()
    if (
        'price' not in item_data
        or 'store_id' not in item_data
        or 'name' not in item_data
    ):
        abort(
            400,
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )
    for item in items.values():
        if (
            item_data['name'] == item['name']
            and item_data['store_id'] == item['store_id']
        ):
            abort(400, message='Item already exists.')

    item_id = uuid.uuid4().hex
    item = {**item_data, 'id': item_id}
    items[item_id] = item

    return item


@app.put('/item/<string:item_id>')
def update_item(item_id):
    item_data = request.get_json()
    if 'price' not in item_data or 'name' not in item_data:
        abort(
            400,
            message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.",
        )
    try:
        item = items[item_id]
        item |= item_data

        return item
    except KeyError:
        abort(404, message='Item not found.')


@app.delete('/item/<string:item_id>')
def delete_item(item_id):
    try:
        del items[item_id]
        return {'message': 'Item deleted.'}
    except KeyError:
        abort(404, message='Item not found.')
