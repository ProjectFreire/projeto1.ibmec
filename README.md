# API Calculadora de Frete

Projeto desenvolvido como parte da disciplina de **MBA** (PROJETO FINAL) para construção de uma **API de Lógica de Negócio** utilizando **FastAPI**, **Pydantic** e **Pytest**.

A API implementa uma calculadora de frete simples, permitindo estimar o **valor do frete** e o **prazo de entrega** a partir de alguns parâmetros básicos.

---

## Tecnologias utilizadas

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic + pydantic-settings
- Pytest
- httpx (suporte ao TestClient)

---

## Objetivo da API

A API expõe uma lógica de negócio de **cálculo de frete**, considerando:

- Tarifa base
- Custo por quilômetro
- Custo por quilograma
- Tipo de entrega:
  - `normal`
  - `expressa` (aplica fator multiplicador e prazo menor)

Esses parâmetros são configuráveis via código (`src/config.py`) e podem ser lidos de variáveis de ambiente (`.env`).

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>