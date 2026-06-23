from app import app
def test_home_page():
    tester=app.test_client()
    response=tester.get("/")
    
    assert response.ststus_code == 200
    assert b"Welcome to flask ci/cd" in response.data