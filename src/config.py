from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "API Calculadora de Frete"
    environment: str = "development"

    # Parâmetros da lógica de frete
    tarifa_base: float = 10.0
    custo_por_km: float = 0.05
    custo_por_kg: float = 2.0
    fator_expressa: float = 1.5
    prazo_normal_dias: int = 5
    prazo_expressa_dias: int = 2

    # Configuração para ler o .env
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()