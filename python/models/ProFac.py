class ProFac:
    def __init__(self, id, idproducto, idfactura, cantidad, precio):
        self.id = id
        self.idproducto = idproducto
        self.idfactura = idfactura
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        return (f"ProFac(id={self.id}, idproducto={self.idproducto}, idfactura={self.idfactura}, "
                f"cantidad={self.cantidad}, precio={self.precio})")
    
    def calcular_total(self):
        """Calcula el total de la línea multiplicando la cantidad por el precio unitario."""
        return self.cantidad * self.precio
