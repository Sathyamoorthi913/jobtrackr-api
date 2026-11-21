from fastapi import FastAPI
app=FastAPI(title="jobtracker API")
@app.get("/")
def home():
    return{"message":"job tracker API is running"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"hello {name}"}

@app.get("/add")
def add(a: int, b:int):
    return{"result":a+b}