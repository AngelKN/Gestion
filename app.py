from flask import Flask
from flask import send_from_directory
from flask import render_template, request, redirect, session
import os.path
import CRUD

app = Flask(__name__)
app.secret_key = "develoteca"

import json

@app.route('/img/<imagen>')
def imagenes(imagen):
    return send_from_directory(os.path.join('img'),imagen)

@app.route("/styles/<archivocss>")
def css_link(archivocss):
    return send_from_directory(os.path.join('styles'),archivocss)

@app.route("/scripts/<js>")
def js_link(js):
    return send_from_directory(os.path.join('scripts'),js)

@app.route("/")
def user():
    return render_template('user/index.html')

@app.route("/vender")
def vender():

    productos = CRUD.getProducto()

    #CRUD.deleteFacturas()
    #CRUD.deleteProFac()

    return render_template('user/vender.html', productos = productos)

@app.route("/vender/factura", methods = ['POST'])
def postFactura():

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
    
    return ("/vender")

@app.route("/admin/")
def admin():

    totalD = CRUD.getTotalD()
    totalM = CRUD.getTotalM()

    facturas = CRUD.getFacturas()

    return render_template('admin/index.html', totalD = totalD, totalM = totalM, facturas = facturas)

@app.route("/admin/producto", methods = ['GET', 'POST'])
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

    return render_template('admin/producto.html', productos = productos, pro = pro, val = val)

@app.route("/admin/factura", methods = ['POST'])
def verFactura():

    id = request.form['id']

    factura = CRUD.getFacturaId(id)
    detalles = CRUD.getProFacId(id)
    print(detalles)
    
    return render_template('admin/factura.html', factura = factura, detalles = detalles)

@app.route("/admin/producto/guardar", methods = ['POST'] )
def postProducto():

    id = request.form['id']
    producto = request.form['producto']
    cantidad = request.form['cantidad']
    vcompra = request.form['vcompra']
    vventa = request.form['vventa']
    val = int(request.form['val'])
    print(val)

    if val == 1:
        CRUD.postProducto(producto, cantidad, vcompra, vventa)
    else:
        CRUD.updateProdcutoFull(id, producto, cantidad, vcompra, vventa)

    return redirect('/admin/producto')

@app.route("/admin/producto/menos", methods = ['POST'] )
def menosProducto():
    id = request.form['id']

    CRUD.updateProdcutoMenos(id)
    return redirect('/admin/producto')

@app.route("/admin/producto/mas", methods = ['POST'] )
def masProducto():
    id = request.form['id']

    CRUD.updateProdcutoMas(id)
    return redirect('/admin/producto')

@app.route("/admin/producto/delete", methods = ['POST'] )
def deleteProducto():
    id = request.form['id']

    CRUD.deleteProducto(id)
    return redirect('/admin/producto')

if __name__ == '__main__':

    app.run(debug=True)