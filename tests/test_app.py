import sys
sys.path.append('../src/')
import app

def test_hello():
    client = app.app.test_client()
    response = client.get("/")
    assert response.data == b"Hello, world!"
