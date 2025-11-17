from flask import Flask, request, render_template, send_file, session
from gerar_qrcode import GerarQR
import requests

app = Flask(__name__)
qr = GerarQR("")

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = None
    if request.method == "POST":
        url = request.form.get('url')

        gerador = GerarQR(url)
        qr_code = gerador.gerar_qr_cod()

    return render_template("index.html", qr_code=qr_code)
    
if __name__ == "__main__":
    app.run(debug=True)