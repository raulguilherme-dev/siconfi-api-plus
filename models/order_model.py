from pydantic import BaseModel

class Order(BaseModel):
    order_by: str = None
    reverse: bool = False