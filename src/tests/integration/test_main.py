from ...app.main import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


def test_get_root():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'hello, world'}


@pytest.mark.parametrize('endpoint, input, output', [
    ('fibonacci', 99, 218922995834555169026),
    ('fizzbuzz', 14, 14),
    ('fizzbuzz', 40, 'buzz'),
    ('fizzbuzz', 60, 'fizzbuzz'),
    ('fizzbuzz', 9, 'fizz'),
])
def test_calculate(endpoint, input, output):
    response = client.get(f'/{endpoint}/{input}')

    assert response.status_code == 200
    assert response.json() == {
        'input': input,
        'output': output
    }


@pytest.mark.parametrize('endpoint, input', [
    ('fibonacci', -1), ('fizzbuzz', 0)
])
def test_less_than(endpoint, input):
    response = client.get(f'/{endpoint}/{input}')

    assert response.status_code == 400
    assert response.json() == {
        'input': input,
        'output': f'{input} is less than {input + 1}'
    }


@pytest.mark.parametrize('endpoint', ['fibonacci', 'fizzbuzz'])
def test_invalid(endpoint):
    response = client.get(f'/{endpoint}/invalid-input')

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
