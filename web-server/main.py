from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_contact():
    return {'contact': 'Leonardo'}
