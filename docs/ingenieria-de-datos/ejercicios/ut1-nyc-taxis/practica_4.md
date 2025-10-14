---
title: "Práctica 4 — Integración de múltiples fuentes de datos + Prefect"
date: 2025-09-07
author: "Juan Paroli"
---

# 🚕 Integración de múltiples fuentes para analizar el sistema de taxis en NYC

## Contexto

En esta práctica trabajamos con **datasets masivos de NYC Taxi (~3M registros)** y los integramos con información de zonas geográficas (CSV) y un calendario de eventos (JSON).  
El objetivo fue **preparar, limpiar y unir datos heterogéneos** para realizar un análisis exploratorio enriquecido y posteriormente **orquestar un pipeline simple con Prefect**.

## 🎯 Objetivos

- [x] Integrar múltiples fuentes de datos (Parquet, CSV, JSON) en un único dataset.  
- [x] Aplicar técnicas de limpieza, normalización y optimización de memoria para trabajar con millones de registros.  
- [x] Realizar joins robustos (LEFT JOIN vs INNER JOIN) y comprender sus implicancias.  
- [x] Generar análisis exploratorios y métricas de negocio por borough.  
- [ ] Implementar un pipeline simple en **Prefect** con tareas orquestadas.  

## Desarrollo

### 1. Carga de datos:

Comenzamos el análisis importando los datos de distintas fuentes:
      - Taxi trips (`.parquet`)
      - zones (`.csv`)
      - calendar (`.json`)

Se analizó que el dataset contenía un total de 3,066,766 viajes cargados y 19 columnas. El contenido fue registrado durante el período de tiempo **[2008-12-31 23:01:42 a 2023-02-01 00:56:53]**.

Tambien aplicamos una normalización de columnas (pasando sus nombres a minúscula) y cremos un campo `pickup_date` que extrae la fecha sin la hora del viaje. Esta nueva columna se utilizó para hacer un join con el dataset calendar, luego de limpiar los datos.

### 2. Limpieza y optimización:  

Antes de realizar los *JOINS* con las demás tablas se limpiaron los datos para evitar errores.

Primero se relleno de nulos en `passenger_count` con el valor típico 1. Luego se eliminó un total de ~71K registros con valores faltantes críticos. Que trajo una optimización de memoria (ahorro ~8%).  

### Joins:

Realizamos dos **JOINS**:

1. `trips + zones` con **LEFT JOIN** → mantiene todos los viajes aunque algunos no tengan zona asignada.  
2. `trips_zones + calendar` → incorporación de flag `is_special_day`.  

### Análisis descriptivo

Se realizó un análisis descriptivo de los viajes y se puedieron reconocer varios insights:
- Manhattan concentra 88% de los viajes.  
- Queens → viajes más largos.  
- Borough con tarifas más altas: EWR
- EWR → mayor revenue por km.  

Además se analizó temporalmente los viajes y se descubrió que las horas pico por número de viajes son:
- 18:00 - 215,889.0 viajes
- 17:00 - 209,493.0 viajes
- 15:00 - 196,424.0 viajes

Además, se corroboró que viajes más caros se relacionan fuertemente con la cantidad de propina dejada. A más caro el viaje, más propina se deja.



## Evidencias
- **Carga y preview de datos**  
  
```python
  trips = pd.read_parquet(trips_url, engine="fastparquet")
  zones = pd.read_csv(zones_url)
  calendar = pd.read_json(calendar_url)
```
```python
# === PRIMER JOIN: TRIPS + ZONES ===

# 1. Hacer join de trips con zones para obtener información geográfica
print("Realizando join: trips + zones...")
trips_with_zones = trips.merge(zones,   # método principal para unir DataFrames
                                left_on='pulocationid',   # columna de trips que contiene ID de zona de pickup
                                right_on='locationid',  # columna de zones que contiene ID correspondiente
                                how='left')       # tipo de join que mantiene todos los trips

print(f"   Registros antes del join: {len(trips)}")
print(f"   Registros después del join: {len(trips_with_zones)}")
print(f"   Nuevas columnas añadidas: {[col for col in trips_with_zones.columns if col not in trips.columns]}")

# 2. Verificar el resultado del join
print("\nVERIFICACIÓN DEL JOIN:")
print("Conteo por Borough:")
print(trips_with_zones['borough'].value_counts())

# 3. Verificar si hay valores nulos después del join
null_after_join = trips_with_zones['borough'].isna().sum()  # contar nulos en columna borough
print(f"\nViajes sin borough asignado: {null_after_join}")

if null_after_join > 0:
    print("   Algunos viajes no encontraron su zona correspondiente")
    print("   LocationIDs problemáticos:")
    problematic_ids = trips_with_zones[trips_with_zones['borough'].isna()]['pulocationid'].unique()  # filtrar filas con nulos
    print(f"   {problematic_ids}")

# 4. Mostrar muestra del resultado
print("\nMUESTRA DEL DATASET INTEGRADO:")
print(trips_with_zones[['pulocationid', 'borough', 'zone', 'trip_distance', 'total_amount']].head())
```

    Realizando join: trips + zones...
       Registros antes del join: 3066766
       Registros después del join: 3066766
       Nuevas columnas añadidas: ['locationid', 'borough', 'zone', 'service_zone']
    
    VERIFICACIÓN DEL JOIN:
    Conteo por Borough:
    borough
    Manhattan        2715369
    Queens            286645
    Unknown            40116
    Brooklyn           18076
    Bronx               4162
    EWR                  410
    Staten Island        341
    Name: count, dtype: int64
    
    Viajes sin borough asignado: 1647
       Algunos viajes no encontraron su zona correspondiente
       LocationIDs problemáticos:
       [265]
    
    MUESTRA DEL DATASET INTEGRADO:
       pulocationid    borough               zone  trip_distance  total_amount
    0           161  Manhattan     Midtown Center           0.97         14.30
    1            43  Manhattan       Central Park           1.10         16.90
    2            48  Manhattan       Clinton East           2.51         34.90
    3           138     Queens  LaGuardia Airport           1.90         20.85
    4           107  Manhattan           Gramercy           1.43         19.68
    


```python
# === SEGUNDO JOIN: TRIPS_ZONES + CALENDAR ===

# 1. Hacer join con datos de calendario
print("Realizando join: trips_zones + calendar...")
trips_complete = trips_with_zones.merge(calendar,   # mismo método de join que antes
                                         left_on='pickup_date',   # columna de fecha que creamos en trips
                                         right_on='date',  # columna de fecha en calendar
                                         how='left')       # tipo que mantiene todos los trips aunque no haya evento especial

print(f"   Registros antes del join: {len(trips_with_zones)}")
print(f"   Registros después del join: {len(trips_complete)}")

# 2. Crear flag de evento especial
trips_complete['is_special_day'] = trips_complete['special'].fillna('False')  # método para rellenar nulos con valor por defecto

print("\nDISTRIBUCIÓN DE DÍAS ESPECIALES:")
print(trips_complete['is_special_day'].value_counts())
print("\nEjemplos de eventos especiales:")
special_days = trips_complete[trips_complete['is_special_day'] == True]
if len(special_days) > 0:
    print(special_days[['pickup_date', 'special', 'borough']].drop_duplicates())
else:
    print("   No hay eventos especiales en este período")

# 3. Mostrar dataset final integrado
print("\nDATASET FINAL INTEGRADO:")
print(f"   Total registros: {len(trips_complete)}")
print(f"   Total columnas: {len(trips_complete.columns)}")
print(f"   Columnas principales: {['borough', 'zone', 'is_special_day', 'trip_distance', 'total_amount']}")

# 4. Verificar integridad de los datos finales
print("\nVERIFICACIÓN FINAL:")
print("Datos faltantes por columna clave:")
key_columns = ['borough', 'zone', 'trip_distance', 'total_amount', 'is_special_day']
for col in key_columns:
    missing = trips_complete[col].isna().sum()  # verificar nulos en cada columna clave final
    print(f"   {col}: {missing} nulos")
```

    Realizando join: trips_zones + calendar...
       Registros antes del join: 3066766
       Registros después del join: 3066766
    
    DISTRIBUCIÓN DE DÍAS ESPECIALES:
    is_special_day
    False    3066766
    Name: count, dtype: int64
    
    Ejemplos de eventos especiales:
       No hay eventos especiales en este período
    
    DATASET FINAL INTEGRADO:
       Total registros: 3066766
       Total columnas: 28
       Columnas principales: ['borough', 'zone', 'is_special_day', 'trip_distance', 'total_amount']
    
    VERIFICACIÓN FINAL:
    Datos faltantes por columna clave:
       borough: 1647 nulos
       zone: 40116 nulos
       trip_distance: 0 nulos
       total_amount: 0 nulos
       is_special_day: 0 nulos
    
```python
# === ANÁLISIS DE CORRELACIONES NUMÉRICAS ===

# Calcular correlaciones entre variables numéricas
print("Calculando correlaciones entre variables numéricas...")
numeric_cols = ['trip_distance', 'total_amount', 'fare_amount', 'tip_amount']
corr_matrix = trips_complete[numeric_cols].corr()  # método para calcular matriz de correlación

print("\nMatriz de Correlación:")
print(corr_matrix.round(3))

print("\nCorrelaciones más fuertes:")
corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_matrix.iloc[i, j]))

corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
for var1, var2, corr in corr_pairs[:3]:
    print(f"   {var1} vs {var2}: {corr:.3f}")

print("\nINTERPRETACIÓN DE CORRELACIONES:")
print("   > 0.7: Correlación fuerte positiva")
print("   0.3-0.7: Correlación moderada positiva") 
print("   -0.3-0.3: Correlación débil")
print("   < -0.7: Correlación fuerte negativa")
```

    Calculando correlaciones entre variables numéricas...
    
    Matriz de Correlación:
                   trip_distance  total_amount  fare_amount  tip_amount
    trip_distance          1.000         0.016        0.016       0.011
    total_amount           0.016         1.000        0.980       0.710
    fare_amount            0.016         0.980        1.000       0.590
    tip_amount             0.011         0.710        0.590       1.000
    
    Correlaciones más fuertes:
       total_amount vs fare_amount: 0.980
       total_amount vs tip_amount: 0.710
       fare_amount vs tip_amount: 0.590
    
    INTERPRETACIÓN DE CORRELACIONES:
       > 0.7: Correlación fuerte positiva
       0.3-0.7: Correlación moderada positiva
       -0.3-0.3: Correlación débil
       < -0.7: Correlación fuerte negativa
    

## PREGUNTAS FINALES

1. ¿Qué diferencia hay entre un LEFT JOIN y un INNER JOIN?
        
        Usando el left join te quedas con los datos de la tabla, es la que se mantiene, mientras que de la derecha son los valores que se agregan. 
        Usando inner join se hace interseccion de las dos tablas. 

2. ¿Por qué usamos LEFT JOIN en lugar de INNER JOIN para trips+zones?
        
        Porque al hacer left te aseguras que vas a mantener toda la informacion de los viajes agregando las zonas correspondientes a los mismos. Si hicieramos inner vamos a perder la informacion de los trips que no tienen zona asignada. 

3. ¿Qué problemas pueden surgir al hacer joins con datos de fechas?
        
        • Diferencias en el tipo de dato, por ejemplo: string o datetime.
        • Formatos de fecha distintos, por ejemplo: YYYY-MM-DD o DD/MM/YYYY.
        • Valores nulos o fechas faltantes que pueden impedir el join.

4. ¿Cuál es la ventaja de integrar múltiples fuentes de datos?
        
        Nos permite realizar un análisis más completo y contextualizado. Además, se pueden cruzar variables de diferentes bases para descubrir patrones que no serían visibles en un solo dataset; esto enriquece la información y habilita conclusiones más profundos.

5. ¿Qué insights de negocio obtuviste del análisis integrado?
        
        Manhattan concentra la mayoría de los viajes, los viajes en Queens son más largos y costosos en promedio y el mejor revenue por km son de EWR. 
        Hay diferencias claras en el revenue por kilómetro y en la tasa de propinas entre boroughs y los días especiales pueden tener impacto en la distancia y tarifa promedio.