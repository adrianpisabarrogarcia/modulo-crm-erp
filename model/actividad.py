class Actividad():
    id = ""
    descripcion = ""
    fecha_vencimiento = ""
    fecha_limite = ""
    resumen = ""
    tipo = ""

    def __init__(self, id, descripcion, fecha_vencimiento, fecha_limite, resumen, tipo):
        self.id = id
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.fecha_limite = fecha_limite
        self.resumen = resumen
        self.tipo = tipo

    def getId(self):
        return self.id

    def getDescripcion(self):
        return self.descripcion

    def getFechaVencimiento(self):
        return self.fecha_vencimiento

    def getFechaLimite(self):
        return self.fecha_limite

    def getResumen(self):
        return self.resumen

    def getTipo(self):
        return self.tipo

    def setId(self, id):
        self.id = id

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setFechaVencimiento(self, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento

    def setFechaLimite(self, fecha_limite):
        self.fecha_limite = fecha_limite

    def setResumen(self, resumen):
        self.resumen = resumen

    def setTipo(self, tipo):
        self.tipo = tipo

    def toString(self):
        return "Id: "+ self.id +"<br>Descripcion: " + self.descripcion + "<br>Fecha de vencimiento: " + self.fecha_vencimiento + "<br>Fecha limite: " + self.fecha_limite + "<br>Resumen: " + self.resumen + "<br>Tipo: " + self.tipo + "<br><br>"

