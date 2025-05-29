# News Headlines Scraper

This is a simple Python script that extracts headlines and links from a news website and saves them to a CSV file.

Este es un script en Python que extrae titulares y enlaces de una página web de noticias y los guarda en un archivo CSV.

---

## How to Use

1. Install dependencies
pip install -r requirements.txt

2. Run the script

python scraper.py --url https://elpais.com --output headlines.csv

You can also filter headlines by a keyword:
python scraper.py --url https://elpais.com --output sports.csv --seccion deportes

También puedes filtrar los titulares por una palabra clave usando --seccion.

Output
The script generates a CSV file with two columns:

headline – the text of the headline

link – the full URL to the article

El script genera un archivo CSV con dos columnas: el titular y el enlace completo al artículo.

See the demo/ folder for an example.

Consulta la carpeta demo/ para ver un ejemplo.

CLI Arguments
Argument	Description	Descripción (ES)
--url	News site URL	URL de la página de noticias
--output	Output CSV filename	Nombre del archivo CSV de salida
--seccion	Filter headlines by keyword (optional)	Filtrar titulares por palabra clave (opcional)

Requirements
Python 3.8 or higher

Libraries:
requests
beautifulsoup4

Requiere Python 3.8+ y las librerías indicadas arriba.

License
MIT License. You’re free to use, modify, and share it.

Licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

Author
Created by @thegraciastudio 

Creado por @thegraciastudio # news-headlines-scraper