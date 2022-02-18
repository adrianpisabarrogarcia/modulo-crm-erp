class Cliente:
    id = ""
    nombre = ""
    telefono = ""
    email = ""
    web = ""
    direccion = ""
    ciudad = ""

    # CONSTRUCTOR
    def __init__(self, id, nombre, telefono, email, web, direccion, ciudad):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.web = web
        self.direccion = direccion
        self.ciudad = ciudad

    # GETTERS
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getTelefono(self):
        return self.telefono

    def getEmail(self):
        return self.correo_electronico

    def getWeb(self):
        return self.web

    def getDireccion(self):
        return self.direccion

    def getCiudad(self):
        return self.ciudad

    # SETTERS
    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setEmail(self, correo_electronico):
        self.correo_electronico = correo_electronico

    def setWeb(self, web):
        self.web = web

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    # TO STRING
    def toString(self):
        return "Id: " + self.id + "\nNombre: " + self.nombre + "\nTelefono: " + self.telefono + "\nEmail: " + self.email + "\nWeb: " + self.web + "\nDireccion: " + self.direccion + "\nCiudad: " + self.ciudad



