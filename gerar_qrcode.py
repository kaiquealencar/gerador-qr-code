from io import BytesIO
import qrcode
import base64

class GerarQR:
    def __init__(self, data: str):
        self.data = data

   
    def gerar_qr_cod(self):        
        if not self.data:
            raise ValueError("Nenhum dado informado para gerar o Qrcode.")
        
        img = qrcode.make(self.data)

        buffer = BytesIO()
        img.save(buffer, format="png")
        buffer.seek(0)
        
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
