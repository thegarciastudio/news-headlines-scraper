import argparse
import logging
import requests
from bs4 import BeautifulSoup
from typing import Optional
from urllib.parse import urljoin
from typing import List, Tuple
import csv

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extrae titulares y enlaces de una página de noticias y los guarda en un CSV. / "
            "Extracts headlines and links from a news page and saves them to a CSV."
        )
    )
    parser.add_argument(
        "--url",
        required=True,
        help="URL de la página de noticias / News site URL (e.g. https://elpais.com)"
    )
    parser.add_argument(
    "--output",
    required=False,
    default="output.csv",
    help="Output CSV file name (default: output.csv) / Nombre del archivo CSV de salida (por defecto: output.csv)"
    )
    parser.add_argument(
        "--seccion",
        help="Filtrar por palabra clave en titulares / Filter by keyword in headlines (optional)"
    )
    return parser.parse_args()

def fetch_html(url: str) -> Optional[BeautifulSoup]:
    try:
        logging.info(f"Connecting to {url} ...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logging.info("Page successfully downloaded.")
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        logging.error(f"Failed to fetch page: {e}")
        return None

def extraer_titulares(soup: BeautifulSoup, base_url: str, palabra_clave: Optional[str] = None) -> List[Tuple[str, str]]:
    titulares = []

    for tag in soup.find_all(["h1", "h2", "h3"]):
        texto = tag.get_text(strip=True)

        a_tag = tag.find("a")
        enlace = urljoin(base_url, a_tag["href"]) if a_tag and a_tag.has_attr("href") else ""

        if texto:
            if palabra_clave:
                if palabra_clave.lower() in texto.lower():
                    titulares.append((texto, enlace))
            else:
                titulares.append((texto, enlace))

    return titulares

def guardar_csv(titulares: List[Tuple[str, str]], nombre_archivo: str):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["headline", "link"])
        writer.writerows(titulares)
    logging.info(f"{len(titulares)} headlines saved to {nombre_archivo}")
    
def main() -> None:
    args = parse_args()

    soup = fetch_html(args.url)
    if not soup:
        logging.error("Exiting due to fetch error.")
        exit(1)

    headlines = extraer_titulares(soup, args.url, args.seccion)
    if not headlines:
        logging.warning("No headlines matched the criteria.")
        print("⚠️ No headlines found. Check the site structure or try another URL.")
        print("⚠️ No se encontraron titulares. Revisa la estructura del sitio o prueba con otra URL.")
    else:
        guardar_csv(headlines, args.output)
        print(f"\n✅ {len(headlines)} headlines extracted from {args.url}")
        print(f"📄 Saved to: {args.output}")

        print(f"\n{len(headlines)} titulares extraídos desde {args.url}")
        print(f"Guardado en: {args.output}")
        
if __name__ == "__main__":
    main()
