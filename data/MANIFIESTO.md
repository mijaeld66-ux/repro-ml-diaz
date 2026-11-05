
# MANIFIESTO DEL DATASET – SENTRYBOX ENAHO 2025

## 1. Identificación del dataset

| Campo | Información |
|---|---|
| Proyecto | SentryBox |
| Estudiante responsable | Mijael Mathias Diaz Aviles |
| Integrante asignado al entregable individual | 1 |
| Rol en el proyecto grupal | Datos |
| Archivo RAW | sentrybox_enaho2025.csv |
| Archivo PROCESSED | dataset.csv |
| Encuesta de referencia | ENAHO 2025 |
| Institución | Instituto Nacional de Estadística e Informática (INEI) |
| Módulo | 500 – Empleo e Ingresos |
| Variable objetivo | ganancia_neta_mes |
| Tipo de tarea | Regresión |
| Algoritmo individual | Regresión lineal |
| Fecha de preparación inicial registrada | 04/11/2026 |
| Fecha de descarga original | No registrada en la documentación del grupo |

## 2. Fuente y procedencia de los datos

La fuente de información utilizada por el proyecto SentryBox es la Encuesta Nacional de Hogares (ENAHO) 2025, elaborada por el Instituto Nacional de Estadística e Informática (INEI), específicamente el Módulo 500: Empleo e Ingresos.

Archivo oficial de referencia:

`Enaho01a-2025-500.csv`

Fuentes de consulta:

- Portal de microdatos del INEI:
  https://proyectos.inei.gob.pe/microdatos/

- Plataforma Nacional de Datos Abiertos:
  https://www.datosabiertos.gob.pe/dataset/encuesta-nacional-de-hogares-enaho-2025-instituto-nacional-de-estad%C3%ADstica-e-inform%C3%A1tica-%E2%80%93

- Diccionario de datos ENAHO 2025: disponible en el catálogo de datos abiertos del INEI.

### Licencia

La ficha del conjunto ENAHO 2025 en la Plataforma Nacional de Datos Abiertos registra la licencia Open Data Commons Open Database License (ODbL).

La distribución del subconjunto derivado debe conservar la atribución a la fuente original y respetar las condiciones correspondientes de dicha licencia.

El archivo `sentrybox_enaho2025.csv` es un subconjunto de trabajo construido por el equipo y no corresponde a la base completa original del INEI.

La fecha exacta de descarga de los microdatos por parte del grupo no quedó registrada en el informe disponible.

## 3. Proceso de construcción del subconjunto

De acuerdo con el informe grupal de SentryBox, se partió de los microdatos originales de la ENAHO 2025, que contienen 84 853 personas y 1 413 columnas.

El equipo seleccionó personas ocupadas que trabajan como empleadores o independientes en el comercio al por menor, utilizando los códigos CIIU Rev. 4 comprendidos entre 4700 y 4799.

El filtrado produjo inicialmente 4 996 observaciones.

Posteriormente, se excluyeron los registros sin información de ganancias o con ganancia declarada igual a cero, obteniendo un total de 4 765 observaciones.

El archivo de trabajo final se denominó:

`sentrybox_enaho2025.csv`

Este archivo contiene 18 columnas: 17 variables candidatas y una variable objetivo.

Para el pipeline individual se excluye `tiene_trabajadores_pagados` por colinealidad exacta con `es_empleador`. Por ello, el modelo utiliza 16 predictores y una variable objetivo.

## 4. Dimensiones y características

| Característica | RAW | PROCESSED |
|---|---:|---:|
| Filas | 4 765 | 4 765 |
| Columnas | 18 | 18 |
| Duplicados exactos | 0 | 0 |
| Valores faltantes totales | 1 | 1 |
| Valores faltantes en el objetivo | 0 | 0 |
| Valores faltantes en nivel_educativo | 1 | 1 |

La variable objetivo es `ganancia_neta_mes`, que representa la ganancia neta de la ocupación principal durante el mes anterior, correspondiente a la variable P530A de ENAHO.

En el archivo de trabajo, la ganancia presenta una media aproximada de S/ 836.21 y una mediana de S/ 457.

## 5. Diccionario de variables

### 5.1. Variable objetivo

| Variable | Tipo | Descripción |
|---|---|---|
| ganancia_neta_mes | Numérica | Ganancia neta mensual de la ocupación principal, expresada en soles (P530A). |

### 5.2. Variables numéricas utilizadas

| Variable | Tipo | Descripción |
|---|---|---|
| edad | Numérica | Años cumplidos del encuestado (P208A). |
| horas_semana | Numérica | Horas trabajadas la semana pasada en la ocupación principal (P513T). |
| anios_en_ocupacion | Numérica | Tiempo en la ocupación principal, expresado en años (P513A1 + P513A2/12). |
| personas_en_negocio | Numérica | Personas que trabajan en el negocio, incluido el encuestado (P512B). |

### 5.3. Variables categóricas utilizadas

| Variable | Tipo | Descripción |
|---|---|---|
| sexo_mujer | Categórica | Indicador de sexo femenino (P207). |
| estado_civil | Categórica | Estado civil del encuestado (P209). |
| nivel_educativo | Categórica | Último nivel educativo aprobado (P301A). |
| es_empleador | Categórica | Indicador de condición de empleador (P507). |
| ayuda_familiar_no_remunerado | Categórica | Indicador de ayuda de familiares sin pago fijo (P508). |
| registro_sunat | Categórica | Condición de registro en SUNAT: persona jurídica, persona natural con RUC o sin RUC (P510A1). |
| lleva_libros_contables | Categórica | Indicador de tenencia de libros o sistema contable (P510B). |
| tiene_ocupacion_secundaria | Categórica | Indicador de ocupación secundaria (P514). |
| subsector_ciiu | Categórica | Actividad económica según CIIU Rev. 4 (P506R4). |
| dominio | Categórica | Dominio geográfico definido por el INEI. |
| estrato | Categórica | Estrato geográfico definido por el INEI. |
| mes_encuesta | Categórica | Mes de realización de la encuesta. |

### 5.4. Variable excluida del modelo

| Variable | Motivo |
|---|---|
| tiene_trabajadores_pagados | Se excluye por colinealidad exacta con es_empleador en las 4 765 observaciones. |

La auditoría realizada por el grupo identificó que ambas variables presentan correlación de Pearson igual a 1.00.

Por este motivo, se conserva `es_empleador` y se excluye `tiene_trabajadores_pagados` del conjunto de predictores.

## 6. Configuración del modelo individual

El pipeline individual utiliza la siguiente configuración:

**Tipo de tarea:** regresión.

**Variable objetivo:**

`ganancia_neta_mes`

**Algoritmo asignado:**

Regresión lineal mediante `LinearRegression` de scikit-learn.

**Variables numéricas:**

- edad
- horas_semana
- anios_en_ocupacion
- personas_en_negocio

**Variables categóricas:**

- sexo_mujer
- estado_civil
- nivel_educativo
- es_empleador
- ayuda_familiar_no_remunerado
- registro_sunat
- lleva_libros_contables
- tiene_ocupacion_secundaria
- subsector_ciiu
- dominio
- estrato
- mes_encuesta

Resumen:

| Elemento | Cantidad |
|---|---:|
| Columnas del CSV original | 18 |
| Variables numéricas utilizadas | 4 |
| Variables categóricas utilizadas | 12 |
| Total de predictores utilizados | 16 |
| Variable objetivo | 1 |
| Variable excluida por colinealidad | 1 |

## 7. Transformaciones de RAW a PROCESSED

El archivo original de trabajo se conserva sin modificaciones.

La preparación se realiza mediante `src/prepare_data.py`.

Las operaciones implementadas son:

1. Lectura del archivo CSV ubicado en `data/raw/`.
2. Registro de la cantidad inicial de filas.
3. Eliminación de espacios al inicio y al final de los nombres de las columnas mediante `str.strip()`.
4. Eliminación de registros duplicados exactos mediante `drop_duplicates()`.
5. Reemplazo de códigos especiales de datos faltantes únicamente si se configuran en `CODIGOS_FALTANTES`.
6. Eliminación de registros sin valor en la variable objetivo `ganancia_neta_mes`.
7. Validación de la existencia de las columnas configuradas.
8. Verificación de que la variable objetivo sea numérica.
9. Generación del archivo `data/processed/dataset.csv` sin índice de pandas.

En la ejecución realizada:

- No se eliminaron registros duplicados.
- No se eliminaron registros por datos faltantes en el objetivo.
- Se mantuvieron los 4 765 registros.
- Se mantuvieron las 18 columnas del archivo de trabajo.

La configuración utilizada fue:

`CODIGOS_FALTANTES = []`

Por tanto, el pipeline individual no realiza un reemplazo global de códigos 99 o 9999.

El CSV de trabajo contiene cuatro registros con valor 99 en `ganancia_neta_mes`. No se recodifican automáticamente, ya que no se ha confirmado que esos valores monetarios representen datos faltantes.

El único valor nulo identificado en el archivo corresponde a `nivel_educativo`.

## 8. Tratamiento de valores faltantes en el entrenamiento

El valor faltante de `nivel_educativo` se conserva durante la preparación del dataset procesado.

Su tratamiento se realiza dentro del Pipeline de scikit-learn durante la validación cruzada.

Las transformaciones utilizadas son:

### Variables numéricas

- Imputación mediante la mediana.
- Estandarización mediante StandardScaler.

### Variables categóricas

- Imputación mediante la categoría más frecuente.
- Codificación OneHotEncoder con `handle_unknown="ignore"`.

El preprocesamiento se ajusta dentro de cada fold utilizando exclusivamente los datos de entrenamiento de esa partición.

Esto permite evitar la fuga de información entre entrenamiento y validación.

## 9. Huellas de integridad MD5

Las huellas calculadas durante la preparación son:

| Archivo | MD5 |
|---|---|
| data/raw/sentrybox_enaho2025.csv | 79cb9c9fcccd760795c3a28fdc8b35e3 |
| data/processed/dataset.csv | 5caa212fdfd858bb9a4f218d43c94d8d |

Estas huellas permiten identificar el contenido de ambos archivos y comprobar que no hayan sufrido cambios accidentales.

La función utilizada para calcularlas se encuentra en `src/prepare_data.py`.

Las huellas deben volver a calcularse cuando se actualice el dataset.

## 10. Organización de los archivos

| Archivo | Ubicación | Función |
|---|---|---|
| CSV de trabajo original | data/raw/ | Conserva los datos de entrada. |
| Dataset procesado | data/processed/ | Contiene los datos preparados. |
| Resumen de experimentos | results/ | Contiene las métricas de los modelos. |
| Captura de MLflow | docs/ | Evidencia visual de las corridas. |
| Configuración | src/config.py | Define objetivo, variables y algoritmo. |
| Preparación | src/prepare_data.py | Limpia y prepara los datos. |
| Entrenamiento | src/train.py | Entrena y evalúa el modelo. |
| Experimentos | src/run_seeds.py | Registra los resultados en MLflow. |

## 11. Limitaciones y consideraciones

1. El archivo utilizado es un subconjunto de la ENAHO 2025 y no la base oficial completa.
2. La ganancia mensual es autorreportada y puede presentar errores de recuerdo o subdeclaración.
3. No se utilizaron factores de expansión del INEI; por tanto, los resultados describen la muestra y no representan directamente a toda la población de microcomerciantes.
4. La muestra tiene cobertura nacional y no exclusivamente de Lima Metropolitana.
5. El modelo estima ganancia neta mensual, pero no predice directamente morosidad ni incumplimiento crediticio.
6. La variable sexo_mujer se utiliza como predictor, por lo que se requiere una evaluación de posibles sesgos antes de emplear el modelo en decisiones crediticias reales.
7. La licencia y las condiciones de redistribución deben respetar la ficha del conjunto original y las condiciones aplicables a los datos derivados.

## 12. Referencias

Instituto Nacional de Estadística e Informática (INEI). (2025). Encuesta Nacional de Hogares (ENAHO) 2025, Módulo 500: Empleo e Ingresos. Portal de microdatos.

https://proyectos.inei.gob.pe/microdatos/

Plataforma Nacional de Datos Abiertos. Encuesta Nacional de Hogares (ENAHO) 2025 – Instituto Nacional de Estadística e Informática.

https://www.datosabiertos.gob.pe/dataset/encuesta-nacional-de-hogares-enaho-2025-instituto-nacional-de-estad%C3%ADstica-e-inform%C3%A1tica-%E2%80%93

Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825–2830.

https://jmlr.org/papers/v12/pedregosa11a.html

---

**Responsable del documento:** Mijael Mathias Diaz Aviles  
**Proyecto:** SentryBox  
**Curso:** Machine Learning I  
**Entregable:** EC2 – Pipeline de ML reproducible
