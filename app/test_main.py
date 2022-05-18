from fastapi.testclient import TestClient

from scraper import app

client = TestClient(app)

##test scrapping one page
def test_scrapping():
    response = client.get("/scrap/realmadrid/1")
    assert response.status_code == 200

##test scrapping with wrong request
def test_nonexistent_endpoint():
    response = client.get("/wrong")
    assert response.status_code == 404