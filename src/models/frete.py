from enum import Enum
from pydantic import BaseModel, Field


class TipoEntrega(str, Enum):
    normal = "normal"
    expressa = "expressa"


class CalcularFreteRequest(BaseModel):
    peso_kg: float = Field(..., gt=0, description="Peso da encomenda em kg")
    distancia_km: float = Field(..., gt=0, description="Distância em km")
    tipo_entrega: TipoEntrega = TipoEntrega.normal


class DetalhesFrete(BaseModel):
    tarifa_base: float
    custo_por_km: float
    custo_por_kg: float
    fator_tipo_entrega: float


class CalcularFreteResponse(BaseModel):
    valor_frete: float
    prazo_dias: int
    detalhes: DetalhesFrete