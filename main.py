from fastapi import FastAPI,Query
from typing import List
from gerenciamento import gerar_gerenciamento
from models import GerenciamentoSaida
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ou use ["*"] durante o desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/mentoring-management/{mentorado_id}", response_model=List[GerenciamentoSaida])
def retornar_gerenciamento(mentorado_id: int):
    return gerar_gerenciamento(mentorado_id)