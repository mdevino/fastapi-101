from fastapi.testclient import TestClient

from ...main import app


client = TestClient(app)

class TestUsers:
  def test_get_user_me(self):
    response = client.get('/users/me')
    
    assert response.status_code == 200
    assert response.json() == {'user_id': 'current user'}

  
  def test_get_user(self):
    response = client.get('/users/12')
    
    assert response.status_code == 200
    assert response.json() == {'user_id': 12}