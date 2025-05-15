from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class GerenciamentoSaida(BaseModel):
    id: int
    name: str
    mentor_name: str
    mentored_name: str
    scheduled_date: datetime