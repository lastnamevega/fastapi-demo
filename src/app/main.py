from ..lib.fibonacci import fibonacci
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class FibonacciOut(BaseModel):
    input: int
    output: Union[int, str]


@app.get('/')
async def root():
    return {'message': 'hello, world'}


@app.get('/fibonacci/{input}', response_model=FibonacciOut)
async def calculate_fibonacci(input: int, response: Response):
    try:
        result = fibonacci(input)
    except ValueError as value_error:
        response.status_code = status.HTTP_400_BAD_REQUEST
        result = str(value_error)

    return {'input': input, 'output': result}
