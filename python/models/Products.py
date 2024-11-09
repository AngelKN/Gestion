class Products:
    def __init__(self, id, producto, cantidad, vcosto, vventa, fecha):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.vcosto = vcosto
        self.vventa = vventa
        self.fecha = fecha

    def __repr__(self):
        return (f"Producto(id={self.id}, producto='{self.producto}', cantidad={self.cantidad}, "
                f"vcosto={self.vcosto}, vventa={self.vventa}, fecha='{self.fecha}')")
    
    def calcular_ganancia(self):
        """Calcula la ganancia por unidad del producto."""
        return self.vventa - self.vcosto
