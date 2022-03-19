from fastapi.testclient import TestClient

from ...main import app


client = TestClient(app)

class TestModels:
  def test_get_model_alexnet(self):
    response = client.get('/models/alexnet')
    assert response.status_code == 200
    assert response.json() == {"model_name": "alexnet", "message": "Deep Learning FTW!"}

  def test_get_model_lenet(self):
    response = client.get('/models/lenet')
    assert response.status_code == 200
    assert response.json() == {"model_name": "lenet", "message": "LeCNN all the images"}
    
  def test_get_model_resnet(self):
    response = client.get('/models/resnet')
    assert response.status_code == 200
    assert response.json() == {"model_name": "resnet", "message": "Have some residuals"}