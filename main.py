from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return "Welcome to our fastapi server..."

@app.get("/contact")
def contact():
    return "Welcome to our contact page"