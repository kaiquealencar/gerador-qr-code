# Gerador de QR Code

## 1. Estrutura do Projeto
Este projeto é um gerador de QR Code simples e funcional, construído em **Python** com **Flask**. Ele permite criar QR Codes a partir de textos ou links e oferece opções de download em PDF ou como imagem.

### Estrutura de arquivos
gerador-qrcode/
│
├── app.py
├── gerar_qrcode.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
└── README.md

## 2. Tecnologias Utilizadas
- Python 3.x  
- Flask  
- qrcode  
- Pillow  
- Segno  
- Requests  
- Gunicorn (para deploy)  

As dependências completas estão no arquivo requirements.txt.

## 3. Funcionalidades
- Gerar QR Code a partir de qualquer texto ou link.  
- Download automático do QR Code em PDF clicando na imagem.  
- Opção de salvar o QR Code em local personalizado através do botão "Salvar".  
- Interface simples e intuitiva para fácil uso.  

## 4. Instalação e Uso

1. Clone o repositório:

- git clone https://github.com/seuusuario/gerador-qrcode.git
- cd gerador-qrcode

2. Crie um Ambiente Virtual
- python -m venv .venv
- source .venv/bin/activate #Linux/MAC
- .venv\Scripts\activate #windows

3. Instale as dependências
- pip install -r requirements.txt

4. Execute a aplicação:
- python app.py ou flask run

5. Demonstração
- https://gerador-qr-code-litu.onrender.com/
