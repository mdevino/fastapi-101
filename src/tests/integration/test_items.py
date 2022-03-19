from fastapi.testclient import TestClient

from ...main import app

client = TestClient(app)

class TestItems:

  def test_get_all_items(self):
    response = client.get('/items/')
    assert response.status_code == 200
    assert response.json() == [
      { 'item_name': 'Foo'},
      { 'item_name': 'Bar'},
      { 'item_name': 'Baz'}
    ]

  def test_get_all_items_given_skip_and_limit(self):
    response = client.get('/items/?skip=1&limit=1')
    assert response.status_code == 200
    assert response.json() == [
      { 'item_name': 'Bar'}
    ]

  def test_get_item(self):
    response = client.get('/items/2')
    assert response.status_code == 200
    assert response.json() == {'item_id': 2}