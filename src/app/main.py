from fastapi import FastAPI, Response, status
from ..lib.fibonacci import fibonacci

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello, world'}


@app.get('/fibonacci/{input}')
async def calculate_fibonacci(input: int, response: Response):
    try:
        return {
            'input': input,
            'output': fibonacci(input)
        }
    except ValueError as value_error:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'detail': str(value_error)}
