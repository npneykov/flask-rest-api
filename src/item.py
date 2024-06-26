import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db, items
from models.item import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint('Items', __name__, description='Operations on items')


@blp.route('/item/<string:item_id>')
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message='Item not found.')

    def delete(self, item_id):
        try:
            del items[item_id]
            return {'message': 'Item deleted.'}
        except KeyError:
            abort(404, message='Item not found.')

    @blp.arguments(ItemUpdateSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message='Item not found.')


@blp.route('/item')
class ItemList(MethodView):
    def get(self):
        return {'items': list(items.values())}

    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message='An error occurred while inserting the item.')

        return item
