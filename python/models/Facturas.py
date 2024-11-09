class Facturas:
    def __init__(self, id, nombre, email, telefono, fecha, total):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha = fecha
        self.total = total

    def __repr__(self):
        return (f"Cliente(id={self.id}, nombre='{self.nombre}', email='{self.email}', "
                f"telefono='{self.telefono}', fecha='{self.fecha}', total={self.total})")
    
    def actualizar_total(self, nuevo_total):
        """Actualiza el valor total del cliente."""
        self.total = nuevo_total
