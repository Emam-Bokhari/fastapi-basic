from fastapi import FastAPI, Request
from mock_data import products

app=FastAPI()

@app.get("/")
def home():
    return "Welcome to our fastapi server..."

@app.get("/products")
def products_data():
    return products

# get single product
# path parameter
@app.get("/products/{product_id}")
def product_data_by_id(product_id:int):

    for product in products:
        if product.get("id")==product_id:
            return product

    return {
        "error": "No product data found"
    }

# query parameter
@app.get("/greet")
def greet(name:str,age:str):
    return {
        "greet":f"Hello, This is {name} & my age is {age}"
    }

# query parameter another example
@app.get("/query")
def query_example(request:Request):
    query_params=dict(request.query_params)
    return f"My name is {query_params.get("name")} & my age is {query_params.get("age")}"

@app.get("/contact")
def contact():
    return "Welcome to our contact page"