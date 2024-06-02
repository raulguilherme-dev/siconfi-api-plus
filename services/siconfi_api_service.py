from fastapi import HTTPException
import requests
from models.filtros_model import Filtro
from models.order_model import Order
from typing import List
from services import filtro_service, group_by_service, order_data_service, show_only_service

def fetch_data() -> list:
    url = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Falha ao buscar dados. status code: {response.status_code}")
    
    data = response.json()
    return data["items"]


def process_data(data: list, filtros: Filtro, order: Order, count: bool, group_by: str, show_only: List[str]) -> list:

    dados = data
    dados = filtro_service.aplicar_filtro(dados, filtros)
        
    if count:
        return {"total": len(dados)}
    
    if group_by == None:
        dados = order_data_service.order(dados, order)


    dados = group_by_service.group_by(dados, group_by, order)

    dados = show_only_service.show_only(dados, show_only)

    return dados


def verify_parameters(filtros: Filtro, order: Order, count: bool, group_by: str, show_only: List[str]):
    if group_by != None and show_only != None or count == True and group_by != None or count == True and order != None or count == True and show_only != None:
        raise HTTPException(status_code=400, detail="Combinação de parâmetros inválida")
