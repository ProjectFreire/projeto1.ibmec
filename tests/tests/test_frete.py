from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_calcular_frete_normal():
    payload = {
        "peso_kg": 2.5,
        "distancia_km": 100,
        "tipo_entrega": "normal",
    }

    response = client.post("/frete/calcular", json=payload)

    assert response.status_code == 200

    data = response.json()
    # 10 + (0.05*100) + (2*2.5) = 20.0  -> fator 1.0
    assert data["valor_frete"] == 20.0
    assert data["prazo_dias"] == 5


def test_calcular_frete_expressa():
    payload = {
        "peso_kg": 2.5,
        "distancia_km": 100,
        "tipo_entrega": "expressa",
    }

    response = client.post("/frete/calcular", json=payload)

    assert response.status_code == 200

    data = response.json()
    # Mesmo cálculo, mas fator 1.5 -> 30.0
    assert data["valor_frete"] == 30.0
    assert data["prazo_dias"] == 2


def test_calcular_frete_dados_invalidos():
    payload = {
        "peso_kg": 0,          # inválido (gt=0)
        "distancia_km": -10,   # inválido (gt=0)
        "tipo_entrega": "normal",
    }

    response = client.post("/frete/calcular", json=payload)

    # Erro de validação do Pydantic/FastAPI
    assert response.status_code == 422