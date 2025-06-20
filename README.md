
# WebScrapping-Challenge

## 🧾 Descripción

Este proyecto consiste en el desarrollo de scrapers web diseñados para extraer información de productos de supermercados de Florida. El objetivo principal es comparar precios y disponibilidades de productos similares en diferentes tiendas, facilitando así análisis de mercado y toma de decisiones informadas.

En la segunda parte del challenge, los datos extraídos se almacenan en una base de datos relacional, lo que permite realizar análisis avanzados, como identificar los productos con mayor dispersión de precios entre cadenas y tiendas.

---

## 🛠️ Tecnologías utilizadas

* **Lenguaje**: Python 3  
* **Entorno**: Jupyter Notebook  
* **Librerías principales**:
  * `requests`
  * `BeautifulSoup`
  * `pandas`
  * `psycopg2` (para conexión con PostgreSQL)
* **Base de datos**: PostgreSQL
* **Contenedores**: Docker + Docker Compose

---

## 📁 Estructura del proyecto

- `CotscoScrapper.ipynb`: Extrae datos de productos desde el sitio web de Costco.
- `SedanosScrapper.ipynb`: Recopila datos de productos desde Sedano's.
- `SamsClubScrapper.ipynb`: Obtiene información de productos desde Sam's Club. *(Falla por captcha luego de ~1500 productos)*
- `WholeFoodsScrapper.ipynb`: Extrae información de productos desde Whole Foods Market. *(Falta el GTIN/UPC)*

---

## ⚙️ Instrucciones de uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/JuanBonadeo/WebScrapping-Challenge.git
cd WebScrapping-Challenge
````

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Asegurate de tener Python 3 y Jupyter Notebook instalados.

### 3. Ejecutar los notebooks

```bash
jupyter notebook
```

Desde Jupyter podés abrir y correr cada scraper manualmente.

---

Perfecto, Juan. Entonces actualizo el README para **incluir esa instrucción importante**: correr el script `uploader.py` una vez que la base de datos esté levantada. Aquí tenés el bloque modificado e integrado al README final:

---

### 🗄️ Levantar la base de datos (PostgreSQL)

Este proyecto utiliza una base de datos PostgreSQL para persistir los datos extraídos.

#### Requisitos

* Tener instalado [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/)

#### Instrucciones

1. Desde la raíz del proyecto, ejecutar:

   ```bash
   docker-compose up -d
   ```

2. Esto iniciará un contenedor llamado `scrapping-challenge-db` expuesto en el puerto `5432`.

3. Credenciales de acceso:

   * **Host**: `localhost`
   * **Puerto**: `5432`
   * **Usuario**: `postgres`
   * **Contraseña**: `123456`
   * **Base de datos**: `scrapping-challenge`

4. Una vez que la base de datos esté corriendo, ejecutá el siguiente script para **crear el esquema** e **insertar los datos** existentes:

   ```bash
   python uploader.py
   ```

   > Este script se conecta a la base de datos, crea todas las tablas necesarias y sube los datos scrapeados que ya se encuentran disponibles en archivos CSV o similares.

5. Para detener el servicio:

   ```bash
   docker-compose down
   ```

---

¿Querés que también documente brevemente qué hace `uploader.py` o qué archivos espera encontrar (por ejemplo, `products.csv`, `stores.csv`, etc.)?


### Requisitos

* Tener instalado [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/)

### Instrucciones

1. Desde la raíz del proyecto, ejecutar:

   ```bash
   docker-compose up -d
   ```

2. Esto iniciará un contenedor llamado `scrapping-challenge-db` expuesto en el puerto `5432`.

3. Credenciales de acceso:

   * **Host**: `localhost`
   * **Puerto**: `5432`
   * **Usuario**: `postgres`
   * **Contraseña**: `123456`
   * **Base de datos**: `scrapping-challenge`

4. Para detener el servicio:

   ```bash
   docker-compose down
   ```

---

## 💾 Persistencia en base de datos

Se diseñó un esquema relacional con las siguientes entidades:

* **Retailers**: cadenas (Costco, Sedano’s, etc.)
* **Stores**: tiendas de Florida
* **Products**: artículos scrapeados
* **Prices**: precios por tienda, producto y fecha

Se seleccionaron **3 tiendas por cadena** y se observaron precios durante un período de **3 a 5 días**.

Los datos se cargan desde los notebooks hacia la base de datos utilizando `psycopg2`.

---

## 📊 Análisis: productos con mayor dispersión de precios

A partir de los datos persistidos, se ejecutó una consulta SQL para obtener el **ranking de los 10 productos con mayor dispersión de precios** entre cadenas y tiendas.
La consulta devuelve:

* **Cadena**
* **Artículo**
* **Tienda**
* **Precio**
* **Fecha de observación**
* **Dispersión** (desvío estándar o diferencia entre precios)

El resultado del análisis se incluye en el informe entregado.

---

## ⚠️ Consideraciones

1. El scraper de Sam's Club se interrumpe por mecanismos de seguridad (CAPTCHA).
2. Los scrapers de Costco y Sedano's funcionan correctamente sobre tiendas de Florida.
3. Whole Foods bloquea IPs de Argentina, se utilizó VPN para el acceso.
4. La carga a base de datos fue realizada solo para un subconjunto representativo (3 tiendas por cadena).

---

## 👤 Autor

**Juan Bonadeo**
🔗 [GitHub](https://github.com/JuanBonadeo)

```

---

```
