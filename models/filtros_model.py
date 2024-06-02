from typing import Optional
from pydantic import BaseModel
from models.population_range_model import PopulationRange

class Filtro(BaseModel):
    capital: Optional[str] = None
    regiao: Optional[str] = None
    uf: Optional[str] = None
    esfera: Optional[str] = None
    exercicio: Optional[int] = None
    populacao: Optional[PopulationRange] = None