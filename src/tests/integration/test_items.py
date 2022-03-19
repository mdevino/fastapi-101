from fastapi.testclient import TestClient

from ...main import app

client = TestClient(app)

class TestItems:

  def test_get_item(self):
    response = client.get('/items/2')
    assert response.status_code == 200
    assert response.json() == {'item_id': 2}