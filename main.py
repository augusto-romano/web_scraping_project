from scraper import get_pdf_links, download_pdfs
from compressor import compress_files

def main():
    links = get_pdf_links()
    download_pdfs(links)
    compress_files()

if __name__ == "__main__":
    main()
