from fastapi import FastAPI, UploadFile


app = FastAPI()

@app.get('/')
def home():
    return {'data': 'welcome to home page'}

@app.get('/contact')
def contact():
    return {'data': "welcome to contact page"}


@app.post('/upload')
def handleUpload(files: list[UploadFile]):
    print(files)
    return {'data': 'uploaded successfully'}


import uvicorn

uvicorn.run(app)