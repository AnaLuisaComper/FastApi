from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_deve_listar_contas_a_pagar_e_receger():
    response = client.get('/contas-a-pagar-e-receber')
                        
    assert response.status_code == 200
    assert response.json()  == [
        {'id': 1, 'descricao': 'Aluguel', 'valor': 10, 'tipo': 'pagar'},
        {'id': 2, 'descricao': 'Internet', 'valor': 10, 'tipo': 'pagar'},
        {'id': 3, 'descricao': 'Salario', 'valor': 1000000000, 'tipo': 'receber'}
        ]
    
    
    
def test_deve_criar_conta_a_pagar_e_receber():
    body={
        "descricao" : "aluguel", 
        "valor" : 10,
        "tipo" : "pagar"
    }
    response = client.post('/contas-a-pagar-e-receber',
    json = body
    )
    assert response.status_code == 201 
    assert response.json() == {'id': 1,
                               'descricao': body['descricao'],
                               'valor': body['valor'],
                               'tipo': body['tipo']
                                }
    
    