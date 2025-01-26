import logging


def test_post_item(client):
    """Check if the item is added to the database"""
    logging.debug(
        client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    )


def test_get_item(client):
    """Check if the response is a dictionary"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    logging.debug(isinstance(client.get('/item/1').json, dict))


def test_get_all_items(client):
    """CHeck if the response is a list"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    client.post('/item', json={'name': 'Test Item2', 'price': 15.99, 'store_id': 1})
    logging.debug(isinstance(client.get('/item').json, (list, dict)))


def test_delete_item(client):
    """Check if the item is deleted from the database"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    client.delete('/item/1')
    logging.debug(client.get('/item/1').status_code == 404)


def test_put_item(client):
    """Check if the item is updated in the database"""
    client.post('/store', json={'store_id': 1, 'name': 'Test Store'})
    client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    client.put('/item/1', json={'name': 'Test Item', 'price': 15.99, 'store_id': 1})
    assert client.get('/item/1').json.get('price') == 15.99
