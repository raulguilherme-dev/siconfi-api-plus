from fastapi import FastAPI, Query
from services.siconfi_api_service import fetch_data, process_data, verify_parameters
from models.filtros_model import Filtro
from models.order_model import Order
from typing import Optional, List
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Mensagem": "Bem vindo"}

@app.get("/get_entes")
async def get_entes(filters: Optional[str] = Query(None), order: Optional[str] = Query(None), count: Optional[bool] = Query(False), group_by: Optional[str] = Query(None), show_only: Optional[str] = Query(None)):
    
    filtro = None
    order_by = None
    show_only_list = None
    
    if filters:
        filtro = Filtro(**json.loads(filters))
    
    if order:
        order_by = Order(**json.loads(order))
    
    if show_only:
        show_only_list = show_only.split("|")
        show_only_list = [x for x in show_only_list]

    verify_parameters(filtro, order_by, count, group_by, show_only_list)   
    
    data = fetch_data()
    
    return process_data(data, filtro, order_by, count, group_by, show_only_list)