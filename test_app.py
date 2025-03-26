from app import app

def test_home():
    response= app.test_client().get("/")

    assert response.statuscode == 200
    assert response.data == "hello"
