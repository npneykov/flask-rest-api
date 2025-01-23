def test_post_item(client):
    """Check if the item is added to the database"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99})
    assert client.get('/item/1').status_code == 200


def test_get_item(client):
    """Check if the response is a dictionary"""
    assert isinstance(client.get('/item/1').json, dict)


def test_get_all_items(client):
    """CHeck if the response is a list"""
    assert isinstance(client.get('/item').json, list)


def test_delete_item(client):
    """Check if the item is deleted from the database"""
    client.delete('/item/1')
    assert client.get('/item/1').status_code == 404


def test_put_item(client):
    """Check if the item is updated in the database"""
    client.post('/item', json={'name': 'Test Item', 'price': 10.99})
    assert client.put('/item/1', json={'price': 15.99}).status_code == 200
