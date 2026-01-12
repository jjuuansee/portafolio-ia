---
title: "Resumen Reflexivo UT4 — Datos No Estructurados"
date: 2025-12-02
author: "Juan Paroli"
---

# 🎵 Reflexión sobre UT4: Datos No Estructurados (Audio)

## ¿De qué trató esta unidad y qué problemas buscaba resolver?

La **UT4** expandió el concepto de "datos" más allá de las tablas estructuradas. Los datos del mundo real vienen en muchas formas: **imágenes**, **audio**, **texto**, **video**. Cada modalidad requiere técnicas específicas de preprocesamiento y extracción de features antes de poder aplicar modelos de ML.

El problema central fue: **¿cómo convertir señales crudas (ondas de audio, píxeles de imagen) en representaciones numéricas que un modelo pueda entender?** Esto implica entender la física de la señal, aplicar transformaciones matemáticas (Fourier, Mel), y extraer features que capturen las características relevantes para la tarea.

En mis palabras, esta unidad me enseñó que **los datos no estructurados son estructurados de otra forma**. Una onda de audio no es "caos"; es una señal con frecuencias, amplitudes y patrones temporales. El trabajo del científico de datos es **revelar esa estructura oculta**.

---

## Conceptos y técnicas clave que incorporé

### 1. **Preprocesamiento de Audio: Estandarización de Señales**

Antes de extraer features, los audios deben tener **formato consistente**. Esto implica normalizar sample rate, duración, canales y amplitud.

**Ejemplo del portafolio**: En la [práctica de Audio](../ejercicios/ut4-audio_as_data/14-audio.ipynb), trabajé con el dataset **UrbanSound8K** (8,732 clips de sonidos urbanos):

**Pipeline de preprocesamiento:**

```python
TARGET_SR = 16000          # Hz (suficiente para voz/sonidos urbanos)
TARGET_DURATION = 3.0      # segundos
TARGET_AMPLITUDE = 0.99    # normalización de pico

def preprocess_audio(path, target_sr, target_duration, top_db=30):
    # 1. Cargar audio
    y, sr = librosa.load(path, sr=None, mono=False)
    
    # 2. Convertir a mono (si es estéreo)
    if y.ndim > 1:
        y = np.mean(y, axis=0)
    
    # 3. Recortar silencios
    y_trim, _ = librosa.effects.trim(y, top_db=top_db)
    
    # 4. Resamplear a sample rate objetivo
    y_rs = librosa.resample(y_trim, orig_sr=sr, target_sr=target_sr)
    
    # 5. Ajustar duración (pad o truncate)
    target_len = int(target_sr * target_duration)
    if len(y_rs) > target_len:
        y_rs = y_rs[:target_len]
    else:
        y_rs = np.pad(y_rs, (0, target_len - len(y_rs)))
    
    # 6. Normalizar amplitud
    max_abs = np.max(np.abs(y_rs)) or 1.0
    y_norm = (TARGET_AMPLITUDE * y_rs) / max_abs
    
    return y_norm.astype(np.float32), target_sr
```

**Justificación de decisiones:**

| Parámetro | Valor | Razón |
|-----------|-------|-------|
| `TARGET_SR = 16000` | 16 kHz | Suficiente para voz/sonidos urbanos (Nyquist: hasta 8 kHz). Reduce tamaño vs 44.1 kHz. |
| `TARGET_DURATION = 3.0` | 3 segundos | Captura eventos urbanos típicos sin exceso de padding. |
| `top_db = 30` | 30 dB | Elimina silencios/ruido de fondo sin perder señal útil. |
| `mono = True` | Mono | Reduce complejidad; información estéreo no es relevante para clasificación. |

**Resultado:**
- **Antes**: 192,000 muestras @ 48 kHz, 4.0s, amplitud [-0.85, 0.81]
- **Después**: 48,000 muestras @ 16 kHz, 3.0s, amplitud [-0.99, 0.93]

---

### 2. **Representaciones Espectrales: De Tiempo a Frecuencia**

El waveform (amplitud vs tiempo) es útil pero no captura la **composición frecuencial** del sonido. Para eso, usamos transformaciones espectrales.

**Short-Time Fourier Transform (STFT):**

La STFT divide la señal en ventanas y aplica la transformada de Fourier a cada una, generando un **espectrograma** (frecuencia vs tiempo).

```python
n_fft = 2048      # tamaño de ventana FFT
hop_length = 512  # avance entre ventanas

D = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
```

**Trade-off resolución:**
- `n_fft` grande → mejor resolución en frecuencia, peor en tiempo
- `n_fft` pequeño → mejor resolución en tiempo, peor en frecuencia

**Espectrograma de Mel:**

El oído humano no percibe frecuencias linealmente; es más sensible a cambios en bajas frecuencias. La escala Mel ajusta las bandas de frecuencia para **imitar la percepción humana**.

```python
mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
```

**Aplicación**: Los espectrogramas Mel son el input estándar para redes neuronales de audio (CNN para clasificación de sonidos).

---

### 3. **MFCCs: Features Compactas para ML Clásico**

Los **Mel-Frequency Cepstral Coefficients (MFCCs)** comprimen la información espectral en ~13-20 coeficientes que representan la "forma" del espectro.

**Extracción de features:**

```python
def extract_mfcc_features(y, sr, n_mfcc=13):
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    feats = {}
    
    # Estadísticas por coeficiente
    for i in range(n_mfcc):
        feats[f"mfcc_{i+1}_mean"] = float(np.mean(mfcc[i, :]))
        feats[f"mfcc_{i+1}_std"] = float(np.std(mfcc[i, :]))
    
    # Features adicionales
    feats["rms_mean"] = float(np.mean(librosa.feature.rms(y=y)))
    feats["zcr_mean"] = float(np.mean(librosa.feature.zero_crossing_rate(y=y)))
    
    return feats  # 28 features total
```

**Interpretación de MFCCs:**

| Coeficiente | Qué captura |
|-------------|-------------|
| `mfcc_1` | Energía global (brillo/volumen) |
| `mfcc_2-4` | Forma general del espectro (timbre) |
| `mfcc_5+` | Detalles finos (textura) |

**Features extraídas para 100 clips:**
- Shape final: **(100, 31)** → 28 features MFCC + 3 metadatos (filename, sr, duration)
- Listas para entrenar modelos clásicos (RandomForest, SVM, etc.)

---

### 4. **Métricas Espectrales Dinámicas**

Más allá de los MFCCs, existen features que describen **cómo cambia el espectro en el tiempo**:

```python
# Centroide espectral: "centro de masa" de las frecuencias
cent = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

# Rolloff: frecuencia bajo la cual está el 85% de la energía
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr, roll_percent=0.85)[0]

# Bandwidth: dispersión del espectro alrededor del centroide
bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
```

**Aplicación**: Estas métricas permiten distinguir entre sonidos "brillantes" (alto centroide: sirenas) y "oscuros" (bajo centroide: motor).

---

## ¿Qué fue lo que más me costó y cómo lo destrabé?

Lo que más me costó fue **entender la relación entre sample rate, frecuencias y el teorema de Nyquist**.

### El problema

Al principio no entendía por qué 16 kHz era "suficiente" para sonidos urbanos. ¿No estamos perdiendo información al reducir desde 44.1 kHz o 48 kHz?

### Cómo lo destrabé

1. **Teorema de Nyquist**: Para capturar una frecuencia `f`, necesitas un sample rate de al menos `2f`. Con 16 kHz, puedo capturar hasta 8 kHz.

2. **Rangos de frecuencia relevantes**:
   - Voz humana: 85 Hz - 8 kHz
   - Sirenas: 500 Hz - 3 kHz
   - Ladridos: 200 Hz - 4 kHz
   - Motor de auto: 20 Hz - 1 kHz

3. **Conclusión**: La mayoría de sonidos urbanos están **por debajo de 8 kHz**. Reducir a 16 kHz:
   - ✅ Mantiene toda la información relevante
   - ✅ Reduce tamaño de datos en ~3x (vs 44.1 kHz)
   - ✅ Reduce tiempo de procesamiento

4. **Verificación práctica**: Comparé espectrogramas a 48 kHz y 16 kHz. Las frecuencias por encima de 8 kHz eran mayormente ruido de fondo, no información útil.

**Lección clave**: Entender la física de la señal permite tomar decisiones informadas sobre preprocesamiento, en lugar de usar valores "por defecto".

---

## Una tarea en detalle: Pipeline de Audio para UrbanSound8K

### ¿Qué hice?

Desarrollé un pipeline completo para procesar audio y extraer features:

1. **Descarga del dataset** desde Kaggle (5.6 GB, 8,732 clips)
2. **Exploración inicial**: Análisis de waveforms, espectrogramas, características
3. **Pipeline de preprocesamiento**: Estandarización de formato
4. **Extracción de features**: MFCCs + métricas espectrales
5. **Exportación**: CSV con 28 features por clip

### ¿Qué aprendí?

1. **El preprocesamiento es crítico**: Sin estandarización, los clips tienen duraciones de 0.5s a 4s, sample rates de 22 kHz a 96 kHz. Esto haría imposible entrenar un modelo consistente.

2. **El recorte de silencios (`trim`) mejora la calidad**: Eliminar silencios al inicio/final concentra la información útil y mejora el ratio señal-ruido efectivo.

3. **MFCCs son poderosos pero no suficientes**: Para tareas complejas, combinar MFCCs con espectrogramas Mel (para CNNs) da mejores resultados.

4. **Augmentation es factible y útil**: `pitch_shift` y `time_stretch` generan variantes del audio para aumentar datos de entrenamiento:

```python
# Pitch shift: subir 2 semitonos
y_pitch = librosa.effects.pitch_shift(y, sr=sr, n_steps=2)

# Time stretch: hacer 10% más lento
y_slow = librosa.effects.time_stretch(y, rate=0.9)
```

5. **Los metadatos del dataset son valiosos**: UrbanSound8K incluye folds predefinidos para cross-validation, evitando que clips del mismo evento (grabados segundos después) aparezcan en train y test.

### ¿Qué mejoraría?

1. **Extraer más features**: Añadir spectral contrast, spectral flatness, tonnetz (para audio musical), chroma features.

2. **Clasificación end-to-end**: Entrenar una CNN sobre espectrogramas Mel en lugar de features manuales.

3. **Data augmentation sistemática**: Crear versiones augmentadas de todos los clips (pitch shift, time stretch, añadir ruido) y evaluar impacto en accuracy.

4. **Análisis por clase**: Ver si diferentes clases de sonido (sirena vs ladrido) tienen diferentes distribuciones de features.

5. **Pipeline en producción**: Crear una función que tome un archivo de audio crudo y retorne la predicción de clase en tiempo real.

---

## ¿En qué tipo de proyecto real usaría esto?

### 1. **Seguridad: Detección de disparos/vidrios rotos**

**Problema**: Sistema de vigilancia que detecta sonidos de emergencia en tiempo real.

**Aplicación UT4**:

- **Preprocesamiento**: Stream de audio continuo, ventanas de 2-3 segundos con overlap.
- **Features**: MFCCs + zero crossing rate (disparos tienen ZCR alto).
- **Modelo**: CNN sobre espectrogramas Mel para detección robusta.
- **Latencia crítica**: Procesamiento en menos de 100ms.

---

### 2. **Salud: Análisis de tos para detección de COVID**

**Problema**: Clasificar grabaciones de tos para screening de enfermedades respiratorias.

**Aplicación UT4**:

- **Preprocesamiento**: Normalización, detección de eventos de tos en grabaciones largas.
- **Features**: MFCCs (capturan timbre de la tos), spectral centroid, duración del evento.
- **Modelo**: Random Forest o CNN sobre espectrogramas.
- **Consideraciones éticas**: Privacidad de audio médico, sesgo por dispositivo de grabación.

---

### 3. **Automotive: Diagnóstico de motor por sonido**

**Problema**: Detectar fallas mecánicas basándose en el sonido del motor.

**Aplicación UT4**:

- **Preprocesamiento**: Filtrado de ruido de viento/camino, normalización por RPM.
- **Features**: Spectral centroid (frecuencia dominante), harmonic-to-noise ratio, anomalías en patrones periódicos.
- **Modelo**: Autoencoder para detección de anomalías (sonidos "anormales" vs "normales").
- **Deployment**: Edge computing en el vehículo.

---

### 4. **Medio ambiente: Monitoreo de biodiversidad**

**Problema**: Identificar especies de aves/mamíferos en grabaciones de campo.

**Aplicación UT4**:

- **Preprocesamiento**: Segmentación de vocalizaciones, separación de fuentes.
- **Features**: MFCCs + chroma (para cantos de aves con estructura melódica).
- **Modelo**: CNN + attention para secuencias largas con múltiples eventos.
- **Escala**: Miles de horas de grabación, procesamiento batch.

---

### 5. **Accesibilidad: Transcripción de audio para sordos**

**Problema**: Generar subtítulos en tiempo real de sonidos no verbales (aplausos, música, sirenas).

**Aplicación UT4**:

- **Preprocesamiento**: VAD (Voice Activity Detection) para separar voz de otros sonidos.
- **Features**: MFCCs para clasificación de sonidos ambientales.
- **Modelo**: Multi-label classification (puede haber múltiples sonidos simultáneos).
- **Output**: "[aplausos]", "[música dramática]", "[sirena de ambulancia]".

---

## Conclusión

La **UT4** expandió mi perspectiva sobre qué significa "datos". Más allá de las tablas CSV, el mundo genera **señales continuas** que pueden analizarse con las técnicas correctas.

Los pilares de esta unidad fueron:

1. ✅ **Estandarización de señales**: Sample rate, duración, canales, amplitud consistentes.
2. ✅ **Representaciones espectrales**: Transformar de tiempo a frecuencia (STFT, Mel).
3. ✅ **Extracción de features**: MFCCs y métricas espectrales para ML clásico.
4. ✅ **Entender la física**: Nyquist, escalas de frecuencia, percepción humana.

Aunque esta unidad se enfocó en audio, los principios aplican a cualquier dato no estructurado:

- **Imágenes**: Estandarizar resolución, extraer features (HOG, SIFT) o usar CNNs.
- **Texto**: Tokenización, embeddings (Word2Vec, BERT).
- **Video**: Combinar técnicas de imagen + audio + series temporales.

El mensaje central es que **los datos no estructurados son estructurados de otra forma**. Nuestro trabajo es encontrar esa estructura y representarla de manera que los modelos puedan aprenderla.

---

## 📚 Referencias

- Librosa Documentation: https://librosa.org/doc/latest/
- UrbanSound8K Dataset: https://www.kaggle.com/datasets/chrisfilo/urbansound8k
- McFee, B., et al. (2015). *librosa: Audio and Music Signal Analysis in Python*.
- Stevens, S. S., Volkmann, J., & Newman, E. B. (1937). *A Scale for the Measurement of the Psychological Magnitude Pitch*. (Escala Mel)
- Scikit-learn: Audio feature extraction

---

