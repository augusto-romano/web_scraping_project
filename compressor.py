import os
import zipfile

DOWNLOAD_DIR = "downloads"
OUTPUT_DIR = "output"
ZIP_FILE = os.path.join(OUTPUT_DIR, "anexos.zip")

def compress_files():
    """ Compacta os arquivos PDF em um único ZIP. """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(DOWNLOAD_DIR):
            for file in files:
                zipf.write(os.path.join(root, file), file)

    print(f"Arquivo ZIP criado: {ZIP_FILE}")

if __name__ == "__main__":
    compress_files()
