from pydantic import BaseModel

class ProductDTO(BaseModel):
    id:int
    product_name:str 
    description:str 
    price:int=0