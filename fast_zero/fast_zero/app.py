from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """hello world usando fast_api
    que irá retorna um json com o conteúdo 'Olá Mundo'"""
    return {'message': 'Olá Mundo!'}
