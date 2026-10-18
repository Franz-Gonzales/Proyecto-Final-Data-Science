"""
Módulo de Auditoría y Evaluación Externa mediante Agente Experto de IA (Lead Data Scientist)
Proyecto: Análisis de Desocupación Juvenil en Bolivia (ECE 4T-2025)
Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca — CEPI
"""

from .audit_engine import AuditEngine, run_full_audit
from .expert_validation_analysis import (
    calcular_v_aiken,
    calcular_alfa_cronbach,
    analizar_respuestas_expertos,
    DIMENSIONES_DEFAULT
)

__all__ = [
    "AuditEngine", 
    "run_full_audit",
    "calcular_v_aiken",
    "calcular_alfa_cronbach",
    "analizar_respuestas_expertos",
    "DIMENSIONES_DEFAULT"
]
