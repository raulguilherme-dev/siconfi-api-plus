from typing import List
from models.order_model import Order

def order(data: List, order: Order) -> list:
    if order == None:
        return data
    
    dados = data
    dados = sorted(dados, key=lambda x: x[order.order_by], reverse=order.reverse)
    return dados


def order_group_by(data: List, order: Order):
    if order == None:
        return data

    dados = data
    if order.order_by == "uf":
        dados = dict(sorted(data.items(), key=lambda x: x[0], reverse=order.reverse))
    elif order.order_by == "total":
        dados = dict(sorted(data.items(), key=lambda x: x[1], reverse=order.reverse))
    return dados