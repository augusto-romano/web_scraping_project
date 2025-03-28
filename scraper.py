import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
DOWNLOAD_DIR = "downloads"

# Definindo os nomes dos arquivos PDF que você quer baixar
PDF_NAME_1 = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
PDF_NAME_2 = "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

def get_pdf_links():
    """ Extrai os links dos arquivos PDF no site. """
    response = requests.get(URL)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        # Faz o link ser absoluto, caso seja relativo
        full_url = urljoin(URL, href)

        # Verifica se o link contém exatamente os arquivos desejados
        if PDF_NAME_1 == full_url.split("/")[-1] or PDF_NAME_2 == full_url.split("/")[-1]:
            pdf_links.append(full_url)
    
    return pdf_links

def download_pdfs(pdf_links):
    """ Faz o download dos arquivos PDF. """
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    for url in pdf_links:
        filename = os.path.join(DOWNLOAD_DIR, url.split("/")[-1])
        print(f"Baixando {filename}...")
        
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
    
    print("Download concluído!")

if __name__ == "__main__":
    links = get_pdf_links()
    download_pdfs(links)
