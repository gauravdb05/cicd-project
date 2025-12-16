import pytest
from app import app as flask_app

@pytest.fixture
def app():
   """Create application fixture for testing."""
   flask_app.config['TESTING'] = True
   return flask_app

@pytest.fixture
def client(app):
    """Create a test client for the application."""
    return app.test_client()


def test_home_endpoint(client):
    """Test home endpoint returns 200 status code."""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "version" in data


def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"

def test_get_users(client):
    """Test get all users"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3

def test_get_user_exists(client):
    """Test get existing user by ID"""
    response = client.get('/api/users/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert "name" in data


def test_get_user_not_exists(client):
    """Test get non-existing user by ID"""
    response = client.get('/api/users/999')
    assert response.status_code == 404
    data = response.get_json()
    assert data["error"] == "User not found"
    