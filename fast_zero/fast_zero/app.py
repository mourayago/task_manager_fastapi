from fastapi import FastAPI 

app = FastAPI()  

@app.get('/')  
def read_root():  
    return {'message': 'Olá Mundo!'}


if __name__ == '__main__':
    print(read_root())