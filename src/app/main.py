from ..lib.fibonacci import fibonacci
from ..lib.fizzbuzz import fizzbuzz
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Out(BaseModel):
    input: int
    output: Union[int, str]


def generate_response(function, input: int, response: Response):
    try:
        output = function(input)
    except ValueError as value_error:
        response.status_code = status.HTTP_400_BAD_REQUEST
        output = str(value_error)

    return Out(input=input, output=output)


@app.get('/')
async def root():
    return {'message': 'hello, world'}


@app.get('/fibonacci/{input}', response_model=Out)
async def calculate_fibonacci_number(input: int, response: Response):
    return generate_response(fibonacci, input, response)


@app.get('/fizzbuzz/{input}', response_model=Out)
async def calculate_fizzbuzz_value(input: int, response: Response):
    return generate_response(fizzbuzz, input, response)
