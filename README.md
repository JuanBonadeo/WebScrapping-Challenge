

# WebScrapping-Challenge

## 🧾 Descripción

Este proyecto consiste en el desarrollo de tres scrapers web diseñados para extraer información de productos de supermercados de Florida. El objetivo principal es comparar precios y disponibilidades de productos similares en diferentes tiendas, facilitando así análisis de mercado y toma de decisiones informadas.

## 🛠️ Tecnologías utilizadas

* **Lenguaje**: Python 3
* **Entorno**: Jupyter Notebook
* **Librerías principales**:

  * `requests`
  * `BeautifulSoup`
  * `pandas`

## 📁 Estructura del proyecto

El repositorio contiene los siguientes notebooks:

* `CotscoScrapper.ipynb`: Extrae datos de productos desde el sitio web de Costco.
* `SedanosScrapper.ipynb`: Recopila datos de productos desde Sedano's.
* `SamsClubScrapper.ipynb`: Obtiene información de productos desde Sam's Club.( le falta poder pasar un captcha )
* `WholeFoodsScrapper.ipynb`: Extrae información de productos desde Whole Foods Market ( le falta el gtin/upc de los products)

## ⚙️ Instrucciones de uso

1. Clona este repositorio:

   ```bash
   git clone https://github.com/JuanBonadeo/WebScrapping-Challenge.git
   cd WebScrapping-Challenge
   ```

2. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

   > Nota: Asegúrate de tener Python 3 y Jupyter Notebook instalados en tu sistema.

3. Abre los notebooks con Jupyter:

   ```bash
   jupyter notebook
   ```

4. Ejecuta cada notebook para realizar el scraping correspondiente.

## 📊 Resultados

Cada scraper genera un DataFrame con la información recopilada, que puede incluir:

* catgeories
* stores
* products
* prices

Estos son exportados a formatos como CSV.

## ⚠️ Consideraciones
1. El scrapper de Sams Club no funciona, tendria que saltearme la seguridad, trae los primero 1500 productos aproximadamente y se corta.

2. Los otros 2 scrappers deberian de correr bien, saque los precios solo de 3 stores como habiamos acordado.

3. En el 4to scrapper que seria el de wholefoods, tuve que utilizar una vpn para poder acceder a la pagina ya que bloqueba ips de Arg.


## 👤 Autor

* **Juan Bonadeo** – [GitHub](https://github.com/JuanBonadeo)

