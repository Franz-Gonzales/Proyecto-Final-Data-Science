"""
Motor Principal de Orquestación de Auditoría de Ciencia de Datos
Proyecto: Análisis de Desocupación Juvenil en Bolivia (ECE 4T-2025)
Autor: Agente Experto IA (Lead Data Scientist Evaluator)
Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca — CEPI
"""

import sys
import time
from pathlib import Path
from typing import Dict, Any, List

from .evaluators import (
    DataEngineeringEvaluator,
    MathematicalConsistencyEvaluator,
    StatisticalInferenceEvaluator,
    SemanticModelBIEvaluator,
    AcademicStorytellingEvaluator,
    PolicyPragmatismEvaluator
)
from .report_generator import (
    generate_radar_chart,
    generate_markdown_report,
    generate_json_scores,
    generate_html_dashboard
)


# Configuración de estilos ANSI para terminal
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


class AuditEngine:
    """Motor central de inspección y auditoría de proyectos de ciencia de datos."""
    
    def __init__(self, project_root: Path = None):
        if project_root is None:
            # Detectar raíz del proyecto subiendo desde src/audit/
            self.project_root = Path(__file__).resolve().parent.parent.parent
        else:
            self.project_root = project_root
            
        self.evaluators = [
            DataEngineeringEvaluator(self.project_root),
            MathematicalConsistencyEvaluator(self.project_root),
            StatisticalInferenceEvaluator(self.project_root),
            SemanticModelBIEvaluator(self.project_root),
            AcademicStorytellingEvaluator(self.project_root),
            PolicyPragmatismEvaluator(self.project_root)
        ]
        
    def run(self) -> Dict[str, Any]:
        """Ejecuta todos los evaluadores y genera los artefactos de auditoría."""
        self._print_header()
        
        results: List[Dict[str, Any]] = []
        total_weight = 0.0
        weighted_score_sum = 0.0
        
        for i, ev in enumerate(self.evaluators, 1):
            print(f"  {CYAN}[{i}/6]{RESET} Inspeccionando {BOLD}{ev.pillar_id}: {ev.pillar_name}{RESET}...", end=" ", flush=True)
            t0 = time.time()
            res = ev.evaluate()
            elapsed = time.time() - t0
            results.append(res)
            
            weight = res["weight"]
            score = res["score"]
            contrib = score * weight
            total_weight += weight
            weighted_score_sum += contrib
            
            score_color = GREEN if score >= 9.5 else (YELLOW if score >= 8.5 else RED)
            print(f"{score_color}{BOLD}{score:.1f}/10.0{RESET} {DIM}({elapsed:.2f}s){RESET}")
            
        # Normalizar promedio ponderado si el total de pesos no suma exactamente 1.0
        global_score = round(weighted_score_sum / total_weight, 2)
        
        if global_score >= 9.0:
            verdict = "APROBADO CON DISTINCIÓN MÁXIMA (EXCELENCIA)"
            verdict_color = GREEN
        elif global_score >= 8.0:
            verdict = "APROBADO CON OBSERVACIONES MENORES"
            verdict_color = BLUE
        elif global_score >= 7.0:
            verdict = "APROBADO REGULAR (REQUIERE MEJORAS)"
            verdict_color = YELLOW
        else:
            verdict = "REPROBADO (NO CUMPLE CRITERIOS MÍNIMOS)"
            verdict_color = RED
            
        summary = {
            "global_score": global_score,
            "global_verdict": verdict,
            "total_pillars": len(results),
            "pillars_approved": sum(1 for r in results if r["score"] >= 7.0),
            "highest_pillar": max(results, key=lambda x: x["score"])["pillar_id"],
            "lowest_pillar": min(results, key=lambda x: x["score"])["pillar_id"],
            "execution_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self._print_summary_table(results, summary, verdict_color)
        
        # Rutas de artefactos de salida
        audits_dir = self.project_root / "outputs" / "audits"
        figures_dir = self.project_root / "outputs" / "figures"
        docs_figures_dir = self.project_root / "docs" / "figures"
        
        audits_dir.mkdir(parents=True, exist_ok=True)
        figures_dir.mkdir(parents=True, exist_ok=True)
        docs_figures_dir.mkdir(parents=True, exist_ok=True)
        
        radar_path = figures_dir / "auditoria_radar_evaluacion.png"
        radar_copy_path = docs_figures_dir / "auditoria_radar_evaluacion.png"
        md_path = audits_dir / "informe_evaluacion_experto_ia.md"
        json_path = audits_dir / "auditoria_scores.json"
        html_path = audits_dir / "dashboard_auditoria.html"
        
        print(f"\n{BOLD}{CYAN}Generando artefactos de auditoría técnica...{RESET}")
        
        # 1. Gráfico Radar
        generate_radar_chart(results, radar_path)
        # Copia para docs/figures
        generate_radar_chart(results, radar_copy_path)
        print(f"  {GREEN}[OK]{RESET} Grafico Radar (300 DPI): {radar_path.relative_to(self.project_root)}")
        
        # 2. Reporte Markdown
        generate_markdown_report(results, summary, md_path)
        print(f"  {GREEN}[OK]{RESET} Informe Markdown: {md_path.relative_to(self.project_root)}")
        
        # 3. JSON estructurado
        generate_json_scores(results, summary, json_path)
        print(f"  {GREEN}[OK]{RESET} Registro JSON estructurado: {json_path.relative_to(self.project_root)}")
        
        # 4. Dashboard Web HTML
        generate_html_dashboard(results, summary, html_path)
        print(f"  {GREEN}[OK]{RESET} Dashboard Interactivo HTML: {html_path.relative_to(self.project_root)}")
        
        print(f"\n{BOLD}{GREEN}[EXITO] Proceso de Auditoria finalizado correctamente.{RESET}\n")
        
        return {
            "summary": summary,
            "pillars": results,
            "artifacts": {
                "radar_chart": str(radar_path),
                "markdown_report": str(md_path),
                "json_scores": str(json_path),
                "html_dashboard": str(html_path)
            }
        }
        
    def _print_header(self):
        print(f"\n{BOLD}{BLUE}========================================================================{RESET}")
        print(f"{BOLD}{CYAN}       AUDITORÍA DE CALIDAD Y EVALUACIÓN CRÍTICA — DATA SCIENCE AI      {RESET}")
        print(f"{BOLD}{BLUE}========================================================================{RESET}")
        print(f"  {DIM}Entorno Académico:{RESET} USFX — CEPI | Diplomado en Data Science")
        print(f"  {DIM}Rol del Agente:{RESET}   Lead Data Scientist & Evaluador Externo Independiente")
        print(f"  {DIM}Proyecto:{RESET}         Desocupación Juvenil en Bolivia (ECE 4T-2025, INE)")
        print(f"{BOLD}{BLUE}------------------------------------------------------------------------{RESET}\n")

    def _print_summary_table(self, results: List[Dict[str, Any]], summary: Dict[str, Any], verdict_color: str):
        print(f"\n{BOLD}{BLUE}------------------------------------------------------------------------{RESET}")
        print(f"{BOLD}{'PILAR':<5} | {'DIMENSIÓN EVALUADA':<38} | {'PESO':<5} | {'NOTA':<5} | {'ESTADO'}{RESET}")
        print(f"{BLUE}------------------------------------------------------------------------{RESET}")
        for r in results:
            print(f"{BOLD}{r['pillar_id']:<5}{RESET} | {r['pillar_name'][:38]:<38} | {r['weight']*100:>4.0f}% | {BOLD}{r['score']:>4.1f}{RESET} | {r['status'][:20]}")
        print(f"{BLUE}------------------------------------------------------------------------{RESET}")
        print(f"{BOLD}{'TOTAL':<5} | {'CALIFICACIÓN GLOBAL PONDERADA':<38} | 100% | {verdict_color}{summary['global_score']:>4.2f}{RESET} | {verdict_color}{summary['global_verdict']}{RESET}")
        print(f"{BOLD}{BLUE}------------------------------------------------------------------------{RESET}")


def run_full_audit(project_root: Path = None) -> Dict[str, Any]:
    """Función de conveniencia para ejecutar la auditoría directa."""
    engine = AuditEngine(project_root)
    return engine.run()
