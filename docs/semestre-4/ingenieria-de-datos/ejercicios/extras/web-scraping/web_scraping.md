---
title: "Web Scraping de Datos con Python"
date: 2025-12-07
author: "Juan Paroli"
---

# 🕷️ Web Scraping de Datos con Python

## Contexto

En este ejercicio se implementaron técnicas de **web scraping** para extraer datos de sitios web usando **BeautifulSoup** y **requests**. El web scraping es una habilidad fundamental en ingeniería de datos para obtener información de fuentes públicas que no tienen APIs disponibles.

## 🎯 Objetivos

- [x] Entender la estructura HTML de páginas web
- [x] Usar requests para obtener contenido de páginas
- [x] Parsear HTML con BeautifulSoup
- [x] Extraer datos estructurados (tablas, listas, texto)
- [x] Manejar paginación y múltiples páginas
- [x] Exportar datos a CSV/DataFrame
- [x] Implementar buenas prácticas (delays, headers, robots.txt)

## Desarrollo

### 1. Instalación

```bash
pip install requests beautifulsoup4 lxml pandas
```

### 2. Estructura básica de scraping

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Headers para simular navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def scrape_page(url):
    """Extrae datos de una página web."""
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        return soup
    else:
        print(f"Error: {response.status_code}")
        return None

# Ejemplo de uso
url = "https://example.com/data"
soup = scrape_page(url)

# Extraer elementos
titles = soup.find_all('h2', class_='title')
prices = soup.find_all('span', class_='price')

# Construir DataFrame
data = []
for title, price in zip(titles, prices):
    data.append({
        'titulo': title.text.strip(),
        'precio': price.text.strip()
    })

df = pd.DataFrame(data)
```

### 3. Selectores CSS y métodos principales

| Método | Uso |
|--------|-----|
| `soup.find()` | Primer elemento que coincide |
| `soup.find_all()` | Todos los elementos que coinciden |
| `soup.select()` | Selector CSS (más flexible) |
| `element.text` | Texto del elemento |
| `element['href']` | Atributo del elemento |
| `element.get('class')` | Obtener atributo (None si no existe) |

### 4. Scraping de tablas HTML

```python
def scrape_table(soup):
    """Extrae datos de una tabla HTML."""
    table = soup.find('table')
    rows = table.find_all('tr')
    
    data = []
    headers = [th.text.strip() for th in rows[0].find_all('th')]
    
    for row in rows[1:]:
        cols = row.find_all('td')
        data.append([col.text.strip() for col in cols])
    
    return pd.DataFrame(data, columns=headers)
```

### 5. Manejo de paginación

```python
def scrape_all_pages(base_url, max_pages=10):
    """Scraping con paginación."""
    all_data = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        soup = scrape_page(url)
        
        if soup is None:
            break
            
        # Extraer datos de la página
        page_data = extract_data(soup)
        all_data.extend(page_data)
        
        # Delay entre requests (respeto al servidor)
        time.sleep(1)
        
        print(f"Página {page} completada")
    
    return pd.DataFrame(all_data)
```

---

## Buenas Prácticas

| Práctica | Descripción |
|----------|-------------|
| **Respetar robots.txt** | Verificar qué páginas se pueden scrapear |
| **Delays entre requests** | Usar `time.sleep()` para no sobrecargar servidores |
| **User-Agent** | Identificarse correctamente |
| **Manejo de errores** | Try-except para conexiones fallidas |
| **Caché** | Guardar respuestas para no repetir requests |
| **Rate limiting** | No hacer más de X requests por minuto |

---

## Herramientas Alternativas

| Herramienta | Uso |
|-------------|-----|
| **Selenium** | Páginas con JavaScript dinámico |
| **Scrapy** | Framework completo para scraping a escala |
| **Playwright** | Automatización de navegador moderna |
| **requests-html** | requests + renderizado JS |

---

## Evidencias

- **Notebook**: [scraping.ipynb](scraping.ipynb)
- **Dataset exportado**: `books_scraped.csv`
- **Sitio scrapeado**: [books.toscrape.com](https://books.toscrape.com/)

---

## Reflexión

El web scraping es una herramienta poderosa pero requiere **responsabilidad**:

- Siempre verificar los términos de servicio del sitio
- No sobrecargar servidores con requests excesivos
- Preferir APIs oficiales cuando estén disponibles
- Considerar aspectos legales según jurisdicción

### Casos de uso válidos

- Agregación de datos públicos
- Monitoreo de precios
- Investigación académica
- Datos sin API disponible

---

## Conclusión

Se implementó un flujo completo de web scraping:

1. ✅ Setup de requests y BeautifulSoup
2. ✅ Parsing de HTML
3. ✅ Extracción de datos estructurados
4. ✅ Manejo de paginación
5. ✅ Exportación a DataFrame/CSV
6. ✅ Buenas prácticas implementadas

---

## Referencias

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://docs.python-requests.org/)
- [Web Scraping Best Practices](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)
- [Scrapy Framework](https://scrapy.org/)

