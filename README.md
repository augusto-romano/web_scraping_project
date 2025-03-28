Web Scraping para Download de Arquivos PDF
Este projeto é uma aplicação simples de web scraping em Python que realiza a extração de links para arquivos PDF específicos em um site e realiza o download desses arquivos para uma pasta local.

Descrição
O script foi desenvolvido para acessar uma página do governo e baixar dois arquivos PDF específicos relacionados ao rol de procedimentos da ANS (Agência Nacional de Saúde Suplementar). O processo de scraping é feito utilizando a biblioteca BeautifulSoup para parsear o HTML da página e a requests para realizar o download dos arquivos.

Funcionalidade Principal:
Acessar o site da ANS.

Extrair os links para arquivos PDF com nomes específicos.

Baixar os arquivos para a pasta local chamada downloads.

Como Funciona
1. Extração dos Links
O script utiliza a biblioteca BeautifulSoup para fazer o parsing do HTML da página e encontra todos os links href="..." que apontam para arquivos PDF. Ele então filtra esses links para garantir que apenas os dois arquivos específicos sejam extraídos com base no nome do arquivo.

2. Download dos Arquivos
A cada link extraído, o script faz o download do arquivo PDF e o salva na pasta downloads no diretório atual. A verificação é feita para garantir que o arquivo baixado seja exatamente o arquivo desejado.

Requisitos
Python 3.x instalado no seu sistema.

Bibliotecas externas:

requests
beautifulsoup4

Você pode instalar as dependências utilizando o pip:

pip install requests beautifulsoup4
Como Usar
Clone o repositório ou faça o download do código.

No terminal, navegue até o diretório onde o código foi salvo.

Execute o script com o comando:

python main.py

Os arquivos PDF especificados serão baixados para a pasta downloads na mesma pasta onde o script está localizado.

Estrutura do Projeto


Personalização
PDF_NAME_1 e PDF_NAME_2 são as variáveis que contêm os nomes dos arquivos PDF a serem baixados. Se precisar de outros arquivos, basta atualizar essas variáveis.

A pasta de download é configurada com o nome downloads, mas você pode alterar o nome da pasta de destino conforme necessário, modificando a variável DOWNLOAD_DIR.