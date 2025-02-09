class TestItems:
    def test_post_item(self, client):
        """Check if the item is added to the database"""
        response = client.post('/store', json={'name': 'Test Store'})
        store_id = response.json.get('id')
        response = client.post(
            '/item',
            json={'name': 'Test Item', 'price': 10.99, 'store_id': store_id},
        )
        assert response.status_code == 201

    def test_get_item(self, client):
        """Check if the response is a dictionary"""
        response = client.post('/store', json={'name': 'Test Store'})
        store_id = response.json.get('id')
        client.post(
            '/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': store_id}
        )
        assert isinstance(client.get('/item/1').json, dict)

    def test_get_all_items(self, client):
        """CHeck if the response is a list"""
        response = client.post('/store', json={'name': 'Test Store'})
        store_id = response.json.get('id')
        client.post(
            '/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': store_id}
        )
        client.post(
            '/item', json={'name': 'Test Item2', 'price': 15.99, 'store_id': store_id}
        )
        assert isinstance(client.get('/item').json, list)

    def test_delete_item(self, client):
        """Check if the item is deleted from the database"""
        response = client.post('/store', json={'name': 'Test Store'})
        store_id = response.json.get('id')
        client.post(
            '/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': store_id}
        )
        response = client.delete('/item/1')
        assert response.status_code == 200

    def test_put_item(self, client):
        """Check if the item is updated in the database"""
        response = client.post('/store', json={'name': 'Test Store'})
        store_id = response.json.get('id')
        client.post(
            '/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': store_id}
        )
        response = client.put('/item/1', json={'name': 'Test Item', 'price': 15.99})
        assert response.json.get('price') == 15.99


class TestStore:
    def test_post_store(self, client):
        """Check if the store is added to the database"""
        response = client.post('/store', json={'name': 'Test Store'})
        assert response.status_code == 201

    def test_get_all_stores(self, client):
        """Check if the response is a dictionary"""
        client.post('/store', json={'name': 'Test Store'})
        client.post('/store', json={'name': 'Test Store2'})
        client.post('/store', json={'name': 'Test Store3'})
        assert isinstance(client.get('/store').json, list)

    def test_delete_store(self, client):
        """Check if the store is deleted from the database"""
        response = client.post('/store', json={'name': 'Test Store'})
        store_id = response.json.get('id')
        response = client.delete(f'/store/{store_id}')
        assert response.status_code == 200


class TestTags:
    def test_get_tags_from_store(self, client):
        """Check if the response is a list"""
        response = client.post('/store', json={'name': 'Test Store'})
        store_id = response.json.get('id')
        response = client.post(f'/store/{store_id}/tag', json={'name': 'Test Tag'})
        assert isinstance(client.get(f'/store/{store_id}/tag').json, list)

    def test_post_tags_to_store(self, client):
        """Check if the tag is added to the database"""
        response = client.post('/store', json={'name': 'Test Store'})
        store_id = response.json.get('id')
        response = client.post(f'/store/{store_id}/tag', json={'name': 'Test Tag'})
        assert response.status_code == 201

    def test_post_tag_to_item(self, client):
        """Check if the tag is added to the database"""
        store_response = client.post('/store', json={'name': 'Test Store'})
        store_id = store_response.json.get('id')
        item_response = client.post(
            '/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': store_id}
        )
        item_id = item_response.json.get('id')
        tag_response = client.post(f'/store/{store_id}/tag', json={'name': 'Test Tag'})
        tag_id = tag_response.json.get('id')
        response = client.post(f'/item/{item_id}/tag/{tag_id}')
        assert response.status_code == 201

    def test_delete_tag_from_item(self, client):
        """Check if the tag is deleted from the database"""
        store_response = client.post('/store', json={'name': 'Test Store'})
        store_id = store_response.json.get('id')
        item_response = client.post(
            '/item', json={'name': 'Test Item', 'price': 10.99, 'store_id': store_id}
        )
        item_id = item_response.json.get('id')
        tag_response = client.post(f'/store/{store_id}/tag', json={'name': 'Test Tag'})
        tag_id = tag_response.json.get('id')
        client.post(f'/item/{item_id}/tag/{tag_id}')
        response = client.delete(f'/item/{item_id}/tag/{tag_id}')
        assert response.status_code == 200

    def test_get_tag(self, client):
        """Check if the tag is added to the database"""
        store_response = client.post('/store', json={'name': 'Test Store'})
        store_id = store_response.json.get('id')
        tag_response = client.post(f'/store/{store_id}/tag', json={'name': 'Test Tag'})
        tag_id = tag_response.json.get('id')
        response = client.get(f'/tag/{tag_id}')
        assert response.status_code == 200

    def test_delete_tag(self, client):
        """Check if the tag is deleted from the database"""
        store_response = client.post('/store', json={'name': 'Test Store'})
        store_id = store_response.json.get('id')
        tag_response = client.post(f'/store/{store_id}/tag', json={'name': 'Test Tag'})
        tag_id = tag_response.json.get('id')
        response = client.delete(f'/tag/{tag_id}')
        assert response.status_code == 200
