from ...app.main import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


def test_get_root():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'hello, world'}


@pytest.mark.parametrize('input, output', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (99, 218922995834555169026),
])
def test_calculate_fibonacci(input, output):
    response = client.get(f'/fibonacci/{input}')

    assert response.status_code == 200
    assert response.json() == {
        'input': input,
        'output': output
    }


def test_fibonacci_less_than():
    input = -1
    response = client.get(f'/fibonacci/{input}')

    assert response.status_code == 400
    assert response.json() == {
        'input': input,
        'output': f'{input} less than 0'
    }


def test_fibonacci_invalid():
    response = client.get(f'/fibonacci/invalid-input')

    assert response.status_code == 422
    assert response.json() == {
        'detail': [{
            'loc': ['path', 'input'],
            'msg':'value is not a valid integer',
            'type':'type_error.integer'
        }]
    }


def test_not_found():
    response = client.get('/nonexistent-endpoint')

    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
