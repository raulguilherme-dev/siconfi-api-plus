from models.filtros_model import Filtro
from typing import List

def aplicar_filtro(data: List, filtros: Filtro) -> list:
    if filtros == None:
        return data

    dados = data
    if filtros.capital != None:
        dados = [d for d in dados if d["capital"] == filtros.capital]
    if filtros.regiao != None:
        dados = [d for d in dados if d["regiao"] == filtros.regiao]
    if filtros.uf != None:
        dados = [d for d in dados if d["uf"] == filtros.uf]
    if filtros.esfera != None:
        dados = [d for d in dados if d["esfera"] == filtros.esfera]
    if filtros.exercicio != None:
        dados = [d for d in dados if d["exercicio"] == filtros.exercicio]
    if filtros.populacao != None:
        dados = [d for d in dados if (filtros.populacao.min is None or d["populacao"] > filtros.populacao.min) and (filtros.populacao.max is None or d["populacao"] < filtros.populacao.max)]


    return dados