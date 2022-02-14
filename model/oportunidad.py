
class Oportunidad():
    id = ""
    actividades = []
    etapa = ""
    clientes = []
    prioridad = ""
    ingreso = ""

    def __init__(self, id, actividades, etapa, clientes, prioridad, ingreso):
        self.id = id
        self.actividades = actividades
        self.etapa = etapa
        self.clientes = clientes
        self.prioridad = prioridad
        self.ingreso = ingreso

    def getId(self):
        return self.id
    def getActividades(self):
        return self.actividades
    def getEtapa(self):
        return self.etapa
    def getClientes(self):
        return self.clientes
    def getPrioridad(self):
        return self.prioridad
    def getIngreso(self):
        return self.ingreso

    def setId(self, id):
        self.id = id
    def setActividades(self, actividades):
        self.actividades = actividades
    def setEtapa(self, etapa):
        self.etapa = etapa
    def setClientes(self, clientes):
        self.clientes = clientes
    def setPrioridad(self, prioridad):
        self.prioridad = prioridad
    def setIngreso(self, ingreso):
        self.ingreso = ingreso

    def __str__(self):
        return "Id: " + str(self.id) + " " + "Oportunidad{ " + "Actividades: " +str(self.actividades) + " " + "Etapa: " + str(self.etapa) + " " + "Clientes: " + str(self.clientes) + " " + "Prioridad: " + str(self.prioridad) + " " +  "Ingreso: " +str(self.ingreso) + " " + " }\n"


