from ...app.main import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


def test_get_root():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'hello, world'}


@pytest.mark.parametrize('number, result', [
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 2),
    (20, 6765),
])
def test_calculate_fibonacci(number, result):
    response = client.get(f'/fibonacci/{number}')

    assert response.status_code == 200
    assert response.json() == {
        'number': number,
        'result': result
    }


def test_fibonacci_less_than():
    num = -1
    response = client.get(f'/fibonacci/{num}')

    assert response.status_code == 400
    assert response.json() == {'detail': f'{num} less than min of 0'}


def test_fibonacci_greater_than():
    num = 21
    response = client.get(f'/fibonacci/{num}')

    assert response.status_code == 400
    assert response.json() == {'detail': f'{num} greater than max of 20'}


def test_not_found():
    response = client.get('/nonexistent-endpoint')

    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
