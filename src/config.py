
"""Configuración del proyecto de Machine Learning."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Zonas del data lake
RAW = ROOT / "data" / "raw" / "sentrybox_enaho2025.csv"
PROCESSED = ROOT / "data" / "processed" / "dataset.csv"
RESULTS = ROOT / "results" / "results_summary.csv"

# Variable que queremos predecir
TARGET = "ganancia_neta_mes"

# Tipo de problema
TAREA = "regresion"

# Variables numéricas
COLS_NUM = [
    "edad",
    "horas_semana",
    "anios_en_ocupacion",
    "personas_en_negocio"
]

# Variables categóricas
COLS_CAT = [
    "sexo_mujer",
    "estado_civil",
    "nivel_educativo",
    "es_empleador",
    "ayuda_familiar_no_remunerado",
    "registro_sunat",
    "lleva_libros_contables",
    "tiene_ocupacion_secundaria",
    "subsector_ciiu",
    "dominio",
    "estrato",
    "mes_encuesta"
]

# No se han especificado códigos especiales de datos faltantes.
CODIGOS_FALTANTES = []

# Algoritmo correspondiente al integrante 1
MODELO = "lineal"

# Semillas establecidas por la profesora
SEMILLA_PARTICION = 42
SEMILLAS = [0, 1, 2, 3, 42]
