from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    """hello world usando fast_api
    que irá retorna um json com o conteúdo 'Olá Mundo'"""
    return {'message': 'Olá Mundo!'}
