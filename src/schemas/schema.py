from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):
    id : Optional[str] = None
    title : str
    year : int
    gender : str
    seasons : int
    
    class Config():
        orm_mode = True