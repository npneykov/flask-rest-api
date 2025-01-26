def test_post_item(client):
    """Check if the item is added to the database"""
    response = client.post(
        '/item',
        json={'name': 'Test Item', 'price': 10.99, 'store_id': 1},
    )
    assert response.status_code == 201


def test_get_item(client):
    """Check if the response is a dictionary"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    assert isinstance(client.get('/item/1').json, dict)


def test_get_all_items(client):
    """CHeck if the response is a list"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    client.post('/item', json={'name': 'Test Item2', 'price': 15.99, 'store_id': 1})
    assert isinstance(client.get('/item').json, list)


def test_delete_item(client):
    """Check if the item is deleted from the database"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    response = client.delete('/item/1')
    assert response.status_code == 200


def test_put_item(client):
    """Check if the item is updated in the database"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': 1})
    response = client.put('/item/1', json={'name': 'Test Item', 'price': 15.99})
    assert response.json.get('price') == 15.99
