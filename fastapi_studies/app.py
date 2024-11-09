from fastapi import FastAPI

app = FastAPI()


@app.get('/')
@app.get('/Son')
def name_son():
    return {'message': 'Andre'}


@app.get('/Brother')
def brother_name():
    return {'message': 'Tiago'}


@app.get('/Mother')
def mother_name():
    return {'message': 'Sonia'}


@app.get('/Father')
def father_name():
    return {'message': 'Mauro'}
