from fastapi import FastAPI, Response, status
from ..lib.fibonacci import fibonacci

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello, world'}


@app.get('/fibonacci/{num}')
async def calculate_fibonacci(num: int, response: Response):
    try:
        return {
            'number': num,
            'result': fibonacci(num)
        }
    except ValueError as value_error:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'detail': str(value_error)}
