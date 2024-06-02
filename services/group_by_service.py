from typing import List
from models.order_model import Order
from services import order_data_service

def group_by(data: List, group_by: str, order: Order):
    if group_by == None:
        return data
    
    dados = data
    data_group_by = {}
    for c, d in enumerate(dados):
        if d[group_by] not in data_group_by.keys():
            data_group_by[d[group_by]] =  1
        elif d[group_by] in data_group_by:
            data_group_by[d[group_by]] += 1

    data_group_by = order_data_service.order_group_by(data_group_by, order)
    return data_group_by