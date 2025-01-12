from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

router= APIRouter(prefix="/contas-a-pagar-e-receber")

class ContaPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: float
    tipo: str # PAGAR, RECEBER
    
class ContaPagarReceberRequest(BaseModel):
    descricao: str
    valor: float
    tipo: str # PAGAR, RECEBER


@router.get("/", response_model=List[ContaPagarReceberResponse])
def listar_contas():
    return[
        ContaPagarReceberResponse(id = 1, descricao = "Aluguel", valor = 10, tipo="pagar"),
        ContaPagarReceberResponse(id = 2, descricao = "Internet", valor = 10, tipo="pagar"),
        ContaPagarReceberResponse(id = 3, descricao = "Salario", valor = 1000000000, tipo="receber"),
    ]
    
@router.post("/", response_model=ContaPagarReceberResponse, status_code=201)    
def criar_conta(conta: ContaPagarReceberRequest):
    return ContaPagarReceberResponse( 
            id = 1, 
            descricao = conta.descricao, 
            valor = conta.valor, 
            tipo=conta.tipo
            )