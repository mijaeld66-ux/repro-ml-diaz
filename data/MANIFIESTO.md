# Manifiesto del dataset – ENAHO 2025

## 1. Identificación

| Campo | Información |
|---|---|
| Nombre del archivo RAW | `sentrybox_enaho2025.csv` |
| Nombre del archivo procesado | `dataset.csv` |
| Proyecto/grupo | [PENDIENTE: nombre del proyecto o grupo] |
| Encuesta de referencia | Encuesta Nacional de Hogares (ENAHO) 2025 |
| Institución de referencia | Instituto Nacional de Estadística e Informática (INEI) |
| Módulo(s) ENAHO utilizado(s) | [PENDIENTE: confirmar con el grupo y el diccionario de datos] |
| Responsable de esta preparación | [NOMBRE Y APELLIDOS] |
| Fecha de descarga/recepción por el grupo | [PENDIENTE: DD/MM/AAAA] |
| Fecha de preparación de este pipeline | 04/11/2026 |
| Versión del archivo de trabajo | 1.0 |

## 2. Fuente y acceso

La fuente estadística de referencia indicada por el grupo es la Encuesta Nacional de Hogares (ENAHO) 2025 del INEI.

- Catálogo de la ENAHO 2025 en la Plataforma Nacional de Datos Abiertos: https://www.datosabiertos.gob.pe/dataset/encuesta-nacional-de-hogares-enaho-2025-instituto-nacional-de-estad%C3%ADstica-e-inform%C3%A1tica-%E2%80%93
- Sistema de Microdatos del INEI: https://proyectos.inei.gob.pe/microdatos/
- URL directa del archivo o módulo del que se obtuvo la información: [PENDIENTE: pegar enlace exacto usado por el grupo].
- Documento/diccionario de variables: [PENDIENTE: nombre y enlace del diccionario usado].
- Licencia indicada en el registro público del conjunto ENAHO 2025: Open Data Commons Open Database License (ODbL). Verificar que el archivo de trabajo `sentrybox_enaho2025.csv` procede del recurso cubierto por ese registro y que la redistribución de esta versión cumple sus condiciones.

**Nota de procedencia:** `sentrybox_enaho2025.csv` es el archivo de trabajo entregado por el grupo (4,765 registros y 18 columnas). No debe describirse como la base completa oficial del INEI, salvo que el grupo pueda demostrarlo. Registrar aquí qué módulos, filtros, uniones o transformaciones se aplicaron para obtener este CSV: [PENDIENTE: completar con el responsable del dataset grupal].

## 3. Descripción y dimensiones

El archivo contiene observaciones utilizadas para modelar la variable `ganancia_neta_mes` a partir de características demográficas, educativas, laborales y del negocio.

| Característica | RAW | PROCESSED |
|---|---:|---:|
| Filas | 4,765 | 4,765 |
| Columnas | 18 | 18 |
| Duplicados exactos | 0 | 0 |
| Valores faltantes totales | 1 | 1 |
| Valores faltantes en `ganancia_neta_mes` | 0 | 0 |

El único valor faltante identificado corresponde a `nivel_educativo`. Se conserva en el archivo PROCESSED y se imputa durante el entrenamiento mediante el `SimpleImputer(strategy="most_frequent")` dentro del Pipeline de scikit-learn. La imputación no se realiza antes de la validación cruzada.

## 4. Diccionario de variables del archivo de trabajo

Las descripciones de esta tabla son orientativas a partir de los nombres de las columnas. Los códigos y categorías deben interpretarse usando el diccionario oficial de ENAHO o el diccionario documentado por el grupo.

| Variable | Uso en el modelo | Tipo configurado | Descripción orientativa |
|---|---|---|---|
| `sexo_mujer` | Predictor | Categórica | Indicador/código de sexo. |
| `edad` | Predictor | Numérica | Edad. |
| `estado_civil` | Predictor | Categórica | Código de estado civil. |
| `nivel_educativo` | Predictor | Categórica | Código de nivel educativo. Presenta 1 valor faltante. |
| `horas_semana` | Predictor | Numérica | Horas trabajadas por semana. |
| `anios_en_ocupacion` | Predictor | Numérica | Años en la ocupación. |
| `personas_en_negocio` | Predictor | Numérica | Número de personas en el negocio. |
| `es_empleador` | Predictor | Categórica | Indicador de condición de empleador. |
| `ayuda_familiar_no_remunerado` | Predictor | Categórica | Indicador de ayuda familiar no remunerada. |
| `tiene_trabajadores_pagados` | Predictor | Categórica | Indicador de trabajadores remunerados. |
| `registro_sunat` | Predictor | Categórica | Código/indicador de registro en SUNAT. |
| `lleva_libros_contables` | Predictor | Categórica | Indicador de tenencia de libros contables. |
| `tiene_ocupacion_secundaria` | Predictor | Categórica | Indicador de ocupación secundaria. |
| `subsector_ciiu` | Predictor | Categórica | Código de subsector CIIU. |
| `dominio` | Predictor | Categórica | Código de dominio. |
| `estrato` | Predictor | Categórica | Código de estrato. |
| `mes_encuesta` | Predictor | Categórica | Mes de encuesta. |
| `ganancia_neta_mes` | Objetivo | Numérica | Ganancia neta mensual que se desea estimar. Confirmar unidad y definición exactas en el diccionario. |

### Configuración de variables

**Objetivo:** `ganancia_neta_mes`  
**Tarea:** regresión  
**Algoritmo asignado al integrante 1:** regresión lineal (`lineal`)

**Predictores numéricos (`COLS_NUM`):**

- `edad`
- `horas_semana`
- `anios_en_ocupacion`
- `personas_en_negocio`

**Predictores categóricos (`COLS_CAT`):**

- `sexo_mujer`
- `estado_civil`
- `nivel_educativo`
- `es_empleador`
- `ayuda_familiar_no_remunerado`
- `tiene_trabajadores_pagados`
- `registro_sunat`
- `lleva_libros_contables`
- `tiene_ocupacion_secundaria`
- `subsector_ciiu`
- `dominio`
- `estrato`
- `mes_encuesta`

## 5. Transformaciones de RAW a PROCESSED

El archivo `data/raw/sentrybox_enaho2025.csv` se conserva sin modificaciones. El script `src/prepare_data.py` realiza las siguientes operaciones:

1. Lee el archivo RAW.
2. Registra la cantidad inicial de filas.
3. Elimina espacios al inicio/final de los nombres de las columnas (`str.strip()`).
4. Elimina registros duplicados exactos (`drop_duplicates()`). En esta ejecución no se eliminó ninguna fila porque se detectaron 0 duplicados.
5. Reemplaza los códigos declarados en `CODIGOS_FALTANTES` por valores nulos. La configuración utilizada fue `CODIGOS_FALTANTES = []`; no se reemplazaron códigos especiales porque no se documentaron códigos adicionales de ausencia.
6. Elimina filas sin valor en la variable objetivo `ganancia_neta_mes`. En esta ejecución no se eliminó ninguna fila porque el objetivo no tenía valores faltantes.
7. Genera `data/processed/dataset.csv` sin guardar el índice de pandas.

El valor nulo de `nivel_educativo` se conserva en PROCESSED. En `src/train.py`, el Pipeline de preprocesamiento realiza la imputación por categoría más frecuente dentro de cada fold. Las variables numéricas se imputan por mediana y luego se estandarizan; las variables categóricas se imputan y codifican mediante One-Hot Encoding. Estas transformaciones se ajustan únicamente con los datos de entrenamiento de cada fold.

## 6. Huellas de integridad (MD5)

| Archivo | MD5 |
|---|---|
| `data/raw/sentrybox_enaho2025.csv` | `79cb9c9fcccd760795c3a28fdc8b35e3` |
| `data/processed/dataset.csv` | `5caa212fdfd858bb9a4f218d43c94d8d` |

Las huellas corresponden a la ejecución local reportada el 04/11/2026. Se pueden recalcular ejecutando `python -m src.prepare_data`. Si cambia el contenido de cualquiera de los archivos, su MD5 probablemente cambiará; por ello, cualquier actualización de datos debe documentarse y generar nuevas huellas.

## 7. Archivos derivados

- RAW: `data/raw/sentrybox_enaho2025.csv`
- PROCESSED: `data/processed/dataset.csv`
- Resultados de experimentos: `results/results_summary.csv`
- Evidencia MLflow: `docs/mlflow.png`

## 8. Notas de uso y restricciones

1. No editar ni sobrescribir manualmente el archivo RAW.
2. No interpretar códigos categóricos sin consultar el diccionario de datos.
3. Confirmar la unidad monetaria y definición de `ganancia_neta_mes` con la documentación del grupo/INEI.
4. Confirmar módulo, filtros y procedimiento de construcción de `sentrybox_enaho2025.csv` antes de publicar este manifiesto.
5. Confirmar las condiciones de la licencia del recurso original antes de distribuir públicamente el CSV RAW o derivados.
6. [PENDIENTE: indicar si el dataset incluye factores de expansión/pesos muestrales y si fueron utilizados en el análisis.]
