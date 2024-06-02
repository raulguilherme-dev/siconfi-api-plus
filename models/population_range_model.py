from pydantic import BaseModel
from typing import Optional

class PopulationRange(BaseModel):
    min: Optional[int] = None
    max: Optional[int] = None