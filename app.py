from flask import Flask, jsonify, send_from_directory, render_template, request, redirect, session
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import base64, os.path, CRUD, smtplib

app = Flask(__name__)
app.secret_key = "develoteca"

import json

def send_email_with_pdf(pdf_path):
    # Configuración del correo electrónico
    from_address = "lolosumine@gmail.com"
    to_address = "redmakota@gmail.com"
    subject = "Tu PDF adjunto"
    body = "Adjunto el archivo PDF solicitado."

    # Credenciales de la cuenta de Gmail
    username = "lolosumine@gmail.com"
    password = ""

    # Configurar el mensaje
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo PDF
    attachment = open(pdf_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(pdf_path)}")
    msg.attach(part)

    # Conectar al servidor SMTP de Gmail y enviar el correo
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print("Correo enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

@app.route('/save-pdf', methods=['POST'])
def save_pdf():
    try:
        # Obtener los datos del PDF en base64 desde la solicitud
        data = request.json['data'].replace('data:application/pdf;base64,', '')
        pdf_data = base64.b64decode(data)

        # Definir la ruta donde se guardará el PDF
        save_path = os.path.join('styles', 'factura.pdf')

        # Crear la carpeta si no existe
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Guardar el archivo PDF
        with open(save_path, 'wb') as pdf_file:
            pdf_file.write(pdf_data)

        #send_email_with_pdf(save_path)

        # Aquí se realiza la eliminación del archivo después de guardarlo
        os.remove(save_path)

        return jsonify({"message": "PDF guardado y eliminado correctamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/img/<imagen>')
def imagenes(imagen):
    return send_from_directory(os.path.join('img'),imagen)

@app.route("/styles/<archivocss>")
def css(archivocss):
    return send_from_directory(os.path.join('styles'),archivocss)

@app.route("/scripts/<js>")
def js(js):
    return send_from_directory(os.path.join('scripts'),js)

@app.route("/templates/<html>")
def html(html):
    return send_from_directory(os.path.join('templates'),html)

@app.route("/")
def user():
    
    return render_template('index.html')

@app.route("/vender", methods = ['GET', 'POST'])
def vender():

    if request.method == 'POST':
        productos = CRUD.getProducto()
        lista = request.get_json()
        print(lista)
        total = lista[-1][0]
        lista = lista[:-1] 
        
        datoCliente = lista[-1]
        lista = lista[:-1]

        if lista:
            fechaFactura = CRUD.postFactura(datoCliente[0],datoCliente[1],datoCliente[2],total)
            idfac = CRUD.getFactura(fechaFactura)

            for lista in lista:
                CRUD.postProFac(idfac[0][0], lista[0], lista[1], lista[2])
                CRUD.updateProdcuto(lista[0], lista[1])

    else:
        productos = CRUD.getProducto()

        #CRUD.deleteFacturas()
        #CRUD.deleteProFac()

    return render_template('vender.html', productos = productos)

@app.route("/home/")
def admin():

    totalD = CRUD.getTotalD()
    totalM = CRUD.getTotalM()

    facturas = CRUD.getFacturas()

    return render_template('home.html', totalD = totalD, totalM = totalM, facturas = facturas)

@app.route("/producto", methods = ['GET', 'POST'])
def nuevoProd():
    if request.method == 'POST':
        pro = []
        id = request.form['id']
        pro = CRUD.getProductoId(id)
        productos = CRUD.getProducto()
        pro = pro[0]
        val = 2
    else:
        productos = CRUD.getProducto()
        pro = []
        val = 1

    return render_template('/productos.html', productos = productos, pro = pro, val = val)

@app.route("/facturas")
def getFacturas():

    facturas = CRUD.getFacturas()

    return render_template('/facturas.html', facturas = facturas)

@app.route("/dia")
def getFacturasD():

    facturas = CRUD.getFacturasD()

    return render_template('/facturas.html', facturas = facturas)

@app.route("/mes")
def getFacturasM():

    facturas = CRUD.getFacturasM()

    return render_template('/facturas.html', facturas = facturas)

@app.route("/año")
def getFacturasA():

    facturas = CRUD.getFacturasA()

    return render_template('/facturas.html', facturas = facturas)


@app.route("/factura", methods = ['POST'])
def verFactura():

    id = request.form['id']

    factura = CRUD.getFacturaId(id)
    profacs = CRUD.getProFacId(id)

    detalles = []
    uno = []

    for profac in profacs:
        idpro = profac[1]
        pro = CRUD.getProductoId(idpro)

        uno.append(profac[0])
        uno.append(pro[0][1])
        uno.append(profac[3])
        uno.append(profac[4])
        detalles.append(uno)
    
    return render_template('factura.html', factura = factura, detalles = detalles)

@app.route("/guardar", methods = ['POST'] )
def postProducto():

    id = request.form['id']
    producto = request.form['producto']
    cantidad = request.form['cantidad']
    vcompra = request.form['vcosto']
    vventa = request.form['vventa']
    val = int(request.form['val'])
    print(val)

    if val == 1:
        CRUD.postProducto(producto, cantidad, vcompra, vventa)
    else:
        CRUD.updateProdcutoFull(id, producto, cantidad, vcompra, vventa)

    return redirect('/producto')

@app.route("/menos", methods = ['POST'] )
def menosProducto():
    id = request.form['id']

    CRUD.updateProdcutoMenos(id)
    return redirect('/producto')

@app.route("/mas", methods = ['POST'] )
def masProducto():
    id = request.form['id']

    CRUD.updateProdcutoMas(id)
    return redirect('/producto')

@app.route("/delete", methods = ['POST'] )
def deleteProducto():
    id = request.form['id']

    CRUD.deleteProducto(id)
    return redirect('/producto')

if __name__ == '__main__':

    app.run(debug=True)