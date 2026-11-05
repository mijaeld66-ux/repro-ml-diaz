# Pipeline de Machine Learning reproducible – ENAHO 2025

**Curso:** Machine Learning 1  
**Entregable:** EC2 – Pipeline de ML reproducible  
**Integrante:** 1  Diaz Aviles Mijael Mathias
**Algoritmo asignado:** Regresión lineal (`lineal`)  
**Variable objetivo:** `ganancia_neta_mes`

> **Antes de publicar:** completa los campos marcados como `[PENDIENTE]`, especialmente el nombre del proyecto/grupo, la URL exacta de origen, la fecha de descarga, la confirmación de la licencia y los datos de la prueba del extraño. No declares que la prueba del extraño se realizó hasta tener el Issue de tu compañero.

## 1. Descripción del proyecto

Este repositorio implementa un pipeline reproducible de Machine Learning para estimar la variable numérica `ganancia_neta_mes` a partir de características de personas, ocupaciones y negocios incluidas en el archivo de trabajo `sentrybox_enaho2025.csv`, preparado por el grupo a partir de información asociada a la Encuesta Nacional de Hogares (ENAHO) 2025.

El estudiante desarrolla el modelo asignado al integrante 1: **regresión lineal** (`LinearRegression` de scikit-learn). El modelo se compara con un baseline de regresión que predice la mediana (`DummyRegressor(strategy="median")`).

El propósito del entregable es que otra persona pueda instalar las dependencias, preparar los datos, ejecutar los experimentos y obtener resultados consistentes con los reportados aquí.

## 2. Datos utilizados

- **Archivo de entrada:** `data/raw/sentrybox_enaho2025.csv`
- **Registros de entrada:** 4,765
- **Columnas:** 18
- **Variable objetivo:** `ganancia_neta_mes`
- **Predictores:** 17 (4 numéricos y 13 categóricos)
- **Registros duplicados detectados:** 0
- **Valores faltantes detectados:** 1, en `nivel_educativo`
- **Valores faltantes en la variable objetivo:** 0
- **Archivo procesado generado:** `data/processed/dataset.csv`

El dataset compartido por el grupo es un archivo de trabajo derivado/seleccionado. Debe conservarse la referencia al módulo, archivo y periodo originales de ENAHO de los que se extrajo. **[PENDIENTE: confirmar con el grupo el módulo exacto, el enlace directo de descarga y si el CSV es la muestra oficial o una selección/transformación del grupo.]**

### Fuente y licencia

- **Institución de referencia:** Instituto Nacional de Estadística e Informática (INEI), Encuesta Nacional de Hogares (ENAHO) 2025.
- **Catálogo de datos abiertos:** https://www.datosabiertos.gob.pe/dataset/encuesta-nacional-de-hogares-enaho-2025-instituto-nacional-de-estad%C3%ADstica-e-inform%C3%A1tica-%E2%80%93
- **Sistema de microdatos del INEI:** https://proyectos.inei.gob.pe/microdatos/
- **Fecha en que el grupo descargó/recibió la fuente:** [PENDIENTE: DD/MM/AAAA].
- **Licencia indicada en el registro del catálogo ENAHO 2025:** Open Data Commons Open Database License (ODbL). **[PENDIENTE: verificar que el archivo específico entregado por el grupo procede de ese recurso y que sus condiciones de redistribución se aplican a esta versión.]**

No se debe asumir que el CSV `sentrybox_enaho2025.csv` es la base oficial completa: el repositorio utiliza el archivo de trabajo proporcionado por el grupo.

## 3. Variables

### Variable objetivo

| Variable | Descripción de trabajo |
|---|---|
| `ganancia_neta_mes` | Ganancia neta mensual que el modelo intenta estimar. Confirmar unidad monetaria y definición exacta con el diccionario del dataset. |

### Predictores numéricos

| Variable | Descripción |
|---|---|
| `edad` | Edad. |
| `horas_semana` | Horas trabajadas por semana. |
| `anios_en_ocupacion` | Años en la ocupación. |
| `personas_en_negocio` | Número de personas en el negocio. |

### Predictores categóricos

| Variable | Descripción |
|---|---|
| `sexo_mujer` | Indicador/código de sexo. |
| `estado_civil` | Código de estado civil. |
| `nivel_educativo` | Código de nivel educativo. |
| `es_empleador` | Indicador de condición de empleador. |
| `ayuda_familiar_no_remunerado` | Indicador de ayuda familiar no remunerada. |
| `tiene_trabajadores_pagados` | Indicador de presencia de trabajadores remunerados. |
| `registro_sunat` | Código/indicador de registro en SUNAT. |
| `lleva_libros_contables` | Indicador de tenencia de libros contables. |
| `tiene_ocupacion_secundaria` | Indicador de ocupación secundaria. |
| `subsector_ciiu` | Código de subsector CIIU. |
| `dominio` | Código de dominio. |
| `estrato` | Código de estrato. |
| `mes_encuesta` | Mes de encuesta. |

> Las descripciones anteriores son etiquetas orientativas basadas en los nombres de las columnas. Para interpretar cada código (por ejemplo, los valores de `estado_civil`, `nivel_educativo`, `dominio` o `estrato`), consultar y citar el diccionario oficial o el diccionario elaborado por el grupo. No interpretar los códigos numéricos como magnitudes continuas.

## 4. Estructura del repositorio

```text
repro-ml/
├── data/
│   ├── raw/
│   │   └── sentrybox_enaho2025.csv
│   ├── processed/
│   │   └── dataset.csv
│   └── MANIFIESTO.md
├── docs/
│   └── mlflow.png
├── results/
│   └── results_summary.csv
├── src/
│   ├── config.py
│   ├── prepare_data.py
│   ├── train.py
│   └── run_seeds.py
├── requirements.txt
├── README.md
└── .gitignore
```

Los directorios `.venv/` y el archivo `mlflow.db` son locales y no deben versionarse. El archivo de datos original solo debe publicarse si la fuente y su licencia autorizan su redistribución; si no, documentar su descarga y mantenerlo fuera de Git.

## 5. Requisitos del entorno

Entorno utilizado para generar los resultados reportados:

- **Python:** 3.14.7
- **Sistema:** Windows, ejecutado desde PowerShell. [PENDIENTE: indicar edición/versión de Windows, por ejemplo Windows 11, si se conoce.]
- **NumPy:** 2.5.4
- **pandas:** 3.1.1
- **scikit-learn:** 1.9.1
- **MLflow:** 3.18.0

Las versiones de dependencias están fijadas en `requirements.txt`.

## 6. Cómo reproducir el proyecto

### 6.1. Windows (PowerShell)

Desde la carpeta raíz del repositorio:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Si PowerShell bloquea la activación del entorno en la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Definir la variable de entorno antes de iniciar Python y preparar los datos:

```powershell
$env:PYTHONHASHSEED = "0"
python -m src.prepare_data
```

Entrenar tres veces con la misma semilla para verificar reproducibilidad:

```powershell
python -m src.train --seed 42 --modelo lineal
python -m src.train --seed 42 --modelo lineal
python -m src.train --seed 42 --modelo lineal
```

Ejecutar los diez experimentos (cinco semillas para baseline y cinco para regresión lineal):

```powershell
python -m src.run_seeds
```

### 6.2. macOS / Linux (bash o zsh)

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
export PYTHONHASHSEED=0
python -m src.prepare_data
```

Verificación de reproducibilidad:

```bash
python -m src.train --seed 42 --modelo lineal
python -m src.train --seed 42 --modelo lineal
python -m src.train --seed 42 --modelo lineal
```

Experimentos:

```bash
python -m src.run_seeds
```

### 6.3. Visualizar los experimentos en MLflow

Después de ejecutar `src.run_seeds`, abrir una segunda terminal con el mismo entorno virtual activado y ejecutar:

```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000
```

Abrir en el navegador: http://127.0.0.1:5000

El experimento se llama `pipeline-reproducible`. Debe mostrar diez corridas: cinco `baseline` y cinco `lineal`.

### 6.4. Archivos que se generan

- `data/processed/dataset.csv`: dataset procesado.
- `results/results_summary.csv`: métricas de las diez corridas.
- `mlflow.db`: base de datos local de MLflow (no subir a Git).

## 7. Diseño experimental y reproducibilidad

- **Tarea:** regresión.
- **Objetivo:** `ganancia_neta_mes`.
- **Modelo asignado:** regresión lineal (`LinearRegression`).
- **Baseline:** `DummyRegressor(strategy="median")`.
- **Partición:** 80 % para desarrollo/validación y 20 % reservado como prueba; el 20 % no se utiliza en este entregable.
- **Validación cruzada:** `KFold(n_splits=5, shuffle=True, random_state=seed)` sobre el 80 % de desarrollo.
- **Semilla de partición:** 42.
- **Semillas de experimentación:** 0, 1, 2, 3 y 42.
- **Preprocesamiento numérico:** imputación por mediana y `StandardScaler`.
- **Preprocesamiento categórico:** imputación por categoría más frecuente y `OneHotEncoder(handle_unknown="ignore")`.
- **Métricas:** MAE, RMSE y R².
- **Registro:** MLflow, experimento `pipeline-reproducible`.

El preprocesamiento está dentro de un `Pipeline` de scikit-learn. En cada fold, los imputadores, el escalador y el codificador se ajustan usando únicamente los datos de entrenamiento de ese fold, evitando que la información del fold de validación intervenga en el ajuste.

El 20 % reservado no se usa para seleccionar ni ajustar el modelo en este entregable.

### Huellas MD5

| Archivo | MD5 |
|---|---|
| RAW `sentrybox_enaho2025.csv` | `79cb9c9fcccd760795c3a28fdc8b35e3` |
| PROCESSED `dataset.csv` | `5caa212fdfd858bb9a4f218d43c94d8d` |

Las huellas identifican el contenido de los archivos utilizados en esta ejecución y permiten detectar cambios accidentales en los datos.

## 8. Resultados

### 8.1. Resultados por semilla

Los valores siguientes corresponden a `results/results_summary.csv` generado por `src.run_seeds`.

| Semilla | Modelo | MAE medio | DE MAE (folds) | RMSE medio | DE RMSE (folds) | R² medio | DE R² (folds) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | baseline | 631.05946 | 67.27055 | 1232.92013 | 162.79982 | -0.09580 | 0.02177 |
| 1 | baseline | 631.10871 | 40.24476 | 1229.40888 | 193.37736 | -0.10137 | 0.03142 |
| 2 | baseline | 630.98995 | 47.19475 | 1229.18997 | 196.00026 | -0.09816 | 0.01257 |
| 3 | baseline | 630.90287 | 49.57325 | 1230.49517 | 184.42108 | -0.09767 | 0.00586 |
| 42 | baseline | 631.32751 | 26.57029 | 1238.08550 | 100.72041 | -0.09552 | 0.01312 |
| 0 | lineal | 573.63000 | 25.52624 | 1006.82720 | 115.72105 | 0.26550 | 0.04579 |
| 1 | lineal | 573.15511 | 36.12376 | 1004.70096 | 179.46112 | 0.26786 | 0.04536 |
| 2 | lineal | 570.97379 | 40.44284 | 1000.80139 | 175.01363 | 0.27495 | 0.03795 |
| 3 | lineal | 575.63808 | 31.17475 | 1011.96512 | 150.63095 | 0.25719 | 0.01752 |
| 42 | lineal | 573.80193 | 19.41010 | 1015.37715 | 92.02921 | 0.26370 | 0.02679 |

### 8.2. Media ± desviación estándar entre semillas

La media y la desviación estándar muestral (ddof=1) se calcularon sobre los cinco valores de `mae_mean`, `rmse_mean` y `r2_mean` de cada modelo. No son las desviaciones estándar internas entre folds que aparecen en las columnas `*_sd` del CSV.

| Modelo | MAE medio ± DE entre semillas | RMSE medio ± DE entre semillas | R² medio ± DE entre semillas |
|---|---:|---:|---:|
| Baseline | 631.07770 ± 0.15966 | 1232.01993 ± 3.69975 | -0.09770 ± 0.00235 |
| Regresión lineal | **573.43978 ± 1.67048** | **1007.93436 ± 5.79228** | **0.26584 ± 0.00645** |

La regresión lineal obtuvo menor MAE y RMSE, y mayor R², que el baseline en las cinco semillas. El MAE medio se redujo aproximadamente 9.13 % respecto al baseline. Esta comparación es descriptiva y no constituye por sí sola una prueba de significancia estadística.

### 8.3. Evidencia de MLflow

La captura de las diez corridas registradas se encuentra en `docs/mlflow.png`.

![Experimentos registrados en MLflow](docs/mlflow.png)

## 9. Limitaciones

1. Se evaluó una regresión lineal; puede no representar relaciones no lineales entre los predictores y la ganancia neta mensual.
2. Los resultados se calcularon mediante validación cruzada sobre el 80 % de desarrollo. El 20 % reservado no se evaluó en este entregable, por lo que no se reporta aquí una métrica final de test.
3. La desviación estándar entre semillas describe la variación de estas particiones/ejecuciones; no es un intervalo de confianza ni garantiza el mismo desempeño en otra muestra o población.
4. Las variables categóricas contienen códigos. Su interpretación depende del diccionario de datos de la fuente.
5. El archivo de trabajo contiene un valor faltante en `nivel_educativo`, imputado dentro del Pipeline durante la validación cruzada.
6. [PENDIENTE: confirmar si el grupo incorporó factores de expansión/pesos muestrales de ENAHO. Si no se usaron, declarar que los resultados del modelo no deben interpretarse como estimaciones representativas de la población peruana.]

## 10. Preguntas de comprensión

**1. ¿Por qué el imputador y el escalador están dentro del Pipeline y no se aplican a todo el dataset antes de la validación cruzada?**  
Porque el imputador y el escalador deben aprender sus parámetros solo con los datos de entrenamiento de cada fold. Si se ajustaran antes sobre todo el dataset, usarían información de los folds de validación y producirían fuga de datos, haciendo que la evaluación fuera demasiado optimista.

**2. ¿Por qué el 20 % de prueba no se utiliza en este entregable? ¿Qué pasaría si lo utilizaras para elegir el modelo?**  
El 20 % queda reservado para una evaluación final independiente y no participa en la selección del modelo en este entregable. Si se utilizara repetidamente para elegir o ajustar el algoritmo, la decisión quedaría adaptada a ese conjunto y dejaría de ser una evaluación independiente.

**3. ¿Qué mide la desviación estándar entre las cinco semillas y qué NO mide?**  
Mide cuánto varían las métricas medias de validación cruzada al cambiar la semilla que determina los folds. Describe estabilidad frente a esas particiones. No mide por sí sola la incertidumbre de toda la población, no es un intervalo de confianza y no garantiza el desempeño en una nueva muestra.

**4. ¿Tu modelo supera al baseline en las cinco semillas? ¿La diferencia es mayor que la desviación estándar? ¿Qué concluyes?**  
Sí. En las cinco semillas, la regresión lineal tuvo menor MAE y RMSE y mayor R². El MAE medio fue 573.43978 frente a 631.07770 del baseline; la diferencia (57.63792) es mayor que las DE entre semillas de ambos modelos. Descriptivamente, la regresión lineal supera al baseline en estas ejecuciones; esto no reemplaza una prueba formal de significancia.

**5. ¿Por qué el archivo RAW nunca se modifica y para qué sirve su MD5?**  
El archivo RAW se conserva intacto para mantener una fuente original verificable y permitir repetir la preparación desde el mismo punto de partida. Su MD5 funciona como huella del contenido y ayuda a detectar si el archivo cambió accidentalmente entre ejecuciones. No se usa como mecanismo de seguridad criptográfica.

**6. ¿Por qué PYTHONHASHSEED=0 debe definirse antes de iniciar Python y no dentro del script?**  
Porque Python lee `PYTHONHASHSEED` al iniciar el intérprete para configurar la aleatorización de los hashes. Cambiar la variable desde el propio script ocurre después de que el intérprete ya inició y no modifica esa configuración del proceso actual. Por eso se define en PowerShell o en la terminal antes de ejecutar Python.

## 11. Prueba del extraño

**Estado:** [PENDIENTE hasta que un compañero de otro grupo clone y ejecute el repositorio].

- Compañero que realizó la prueba: [NOMBRE].
- Grupo: [GRUPO].
- Fecha: [DD/MM/AAAA].
- Resultado: [EXITOSO / CON OBSERVACIONES].
- Issue de GitHub: [URL DEL ISSUE].
- Observaciones/correcciones: [DETALLAR].

No marcar esta prueba como exitosa hasta que el Issue y la ejecución del compañero estén disponibles.

## 12. Declaración de uso de inteligencia artificial

Se utilizó ChatGPT (OpenAI) como herramienta de apoyo para comprender las instrucciones del entregable, interpretar mensajes de error, revisar conceptos de reproducibilidad y orientar la redacción de documentación. La configuración final, ejecución de los comandos, revisión de las salidas y validación de los resultados fueron realizadas por el estudiante, quien es responsable del contenido y puede explicar el código.

## 13. Autor y repositorio

- **Estudiante:** [NOMBRE Y APELLIDOS].
- **Curso:** Machine Learning 1.
- **Repositorio GitHub:** [URL DEL REPOSITORIO PÚBLICO].
- **Grupo/proyecto integrador:** [NOMBRE O TEMA DEL GRUPO].
