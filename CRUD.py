from db import obtener_conexion
from datetime import datetime

def postProducto(producto, cantidad, vcosto,vventas):

    fechaHora = datetime.now().strftime("%d-%m-%Y : %H:%M:%S")

    con = obtener_conexion()
    cursor = con.cursor()
    sql = "INSERT INTO productos (id, producto, cantidad, vcosto, vventa, fecha) VALUES (NULL, '{}', {}, {}, {}, '{}');"
    cursor.execute(sql.format(producto, cantidad, vcosto,vventas,fechaHora))
    con.commit()
    con.close()

def postFactura(nombre, email, telefono, total):
    fechaHora = datetime.now().strftime("%d-%m-%Y : %H:%M:%S")
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "INSERT INTO facturas (id, nombre, email, telefono, fecha, total) VALUES (NULL, '{}', '{}', '{}', '{}', {});".format(nombre, email, telefono, fechaHora, total)
    cursor.execute(sql)
    con.commit()
    con.close()
    return fechaHora

def postProFac( idFac, idPro, cantidad, precio):
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "INSERT INTO pro_fac (id,  idproducto, idfactura, cantidad, precio) VALUES (NULL, {}, {}, {}, {});".format(idPro, idFac, cantidad, precio)
    cursor.execute(sql)
    con.commit()
    con.close()

def getProducto():
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM productos"
    cursor.execute(sql)
    produc = cursor.fetchall()
    con.commit()
    con.close()
    return produc

def getProductoId(id):
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM productos WHERE id = {}".format(id)
    cursor.execute(sql)
    produc = cursor.fetchall()
    con.commit()
    con.close()
    return produc

def getFactura(fechaFactura):
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "SELECT id FROM facturas WHERE facturas.fecha = '{}'".format(fechaFactura)
    cursor.execute(sql)
    idfactura = cursor.fetchall()
    con.commit()
    con.close()
    return idfactura

def getFacturaId(id):
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM facturas WHERE facturas.id = {}".format(id)
    cursor.execute(sql)
    factura = cursor.fetchall()
    con.commit()
    con.close()
    return factura

def getFacturas():
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM facturas"
    cursor.execute(sql)
    facturas = cursor.fetchall()
    con.commit()
    con.close()
    return facturas

def getProFacId(id):
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM pro_fac WHERE idfactura = {}".format(id)
    cursor.execute(sql)
    facturas = cursor.fetchall()
    con.commit()
    con.close()
    return facturas

def getTotalD():

    fechaHora = datetime.now().strftime("%d-%m-%Y")
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "SELECT total FROM facturas WHERE fecha LIKE '{}%'".format(fechaHora)
    cursor.execute(sql)
    totalD = cursor.fetchall()

    total = 0

    for totalD in totalD:
        total = total + totalD[0]

    con.commit()
    con.close()
    return total

def getTotalM():

    fechaHora = datetime.now().strftime("%m-%Y")
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "SELECT total FROM facturas WHERE fecha LIKE '%{}%'".format(fechaHora)
    cursor.execute(sql)
    totalD = cursor.fetchall()

    total = 0

    for totalD in totalD:
        total = total + totalD[0]

    con.commit()
    con.close()
    return total

def deleteProducto(id):
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "DELETE FROM productos WHERE productos.id = {};".format(id)
    cursor.execute(sql)
    con.commit()
    con.close()

def deleteFacturas():
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "DELETE FROM facturas"
    cursor.execute(sql)
    con.commit()
    con.close()    

def deleteProFac():
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "DELETE FROM pro_fac"
    cursor.execute(sql)
    con.commit()
    con.close() 

def updateProdcuto(idPro, cantidad):
    con = obtener_conexion()
    cursor = con.cursor()
    
    sql = "UPDATE productos SET cantidad = cantidad - {} WHERE id = {}".format(cantidad, idPro)
    cursor.execute(sql)
    con.commit()
    con.close() 

def updateProdcutoMenos(idPro):
    con = obtener_conexion()
    cursor = con.cursor()
    
    sql = "UPDATE productos SET cantidad = cantidad - 1 WHERE id = {}".format(idPro)
    cursor.execute(sql)
    con.commit()
    con.close() 

def updateProdcutoMas(idPro):
    con = obtener_conexion()
    cursor = con.cursor()
    
    sql = "UPDATE productos SET cantidad = cantidad + 1 WHERE id = {}".format(idPro)
    cursor.execute(sql)
    con.commit()
    con.close() 

def updateProdcutoFull(id, producto, cantidad, vcosto, vventas):

    fechaHora = datetime.now().strftime("%d-%m-%Y : %H:%M:%S")
    con = obtener_conexion()
    cursor = con.cursor()
    sql = "UPDATE productos SET producto = '{}', cantidad = {}, vcosto = {}, vventa = {}, fecha = '{}' WHERE id = {}".format(producto, cantidad, vcosto,vventas, fechaHora, id)
    cursor.execute(sql)
    con.commit()
    con.close() 