from fastapi import APIRouter

from src.config import settings
from src.models.frete import (
    CalcularFreteRequest,
    CalcularFreteResponse,
    DetalhesFrete,
    TipoEntrega,
)

router = APIRouter(
    prefix="/frete",
    tags=["frete"],
)


@router.post("/calcular", response_model=CalcularFreteResponse)
def calcular_frete(dados: CalcularFreteRequest) -> CalcularFreteResponse:
    # Define o fator conforme o tipo de entrega
    if dados.tipo_entrega == TipoEntrega.normal:
        fator_tipo = 1.0
        prazo = settings.prazo_normal_dias
    else:
        fator_tipo = settings.fator_expressa
        prazo = settings.prazo_expressa_dias

    # Cálculo do valor do frete
    valor = (
        settings.tarifa_base
        + settings.custo_por_km * dados.distancia_km
        + settings.custo_por_kg * dados.peso_kg
    ) * fator_tipo

    detalhes = DetalhesFrete(
        tarifa_base=settings.tarifa_base,
        custo_por_km=settings.custo_por_km,
        custo_por_kg=settings.custo_por_kg,
        fator_tipo_entrega=fator_tipo,
    )

    return CalcularFreteResponse(
        valor_frete=round(valor, 2),
        prazo_dias=prazo,
        detalhes=detalhes,
    )
