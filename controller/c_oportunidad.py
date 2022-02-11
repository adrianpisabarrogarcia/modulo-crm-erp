from model.oportunidad import Oportunidad

oportunidades = []

# Método que dice cual es el próximo id para generar una nueva oportunidad
def getNextId():
    return len(oportunidades) + 1

# Método para agregar una nueva oportunidad
def anadir_oportunidad(request):
    id = str(getNextId())
    # actividades = str(request.form.get("actividades"))
    etapa = str(request.form.get("telefono"))
    # clientes = str(request.form.get("clientes"))
    prioridad = str(request.form.get("prioridad"))
    ingreso = str(request.form.get("ingreso"))
    correo = str(request.form.get("correo"))

    actividades = []
    clientes = []
    oportunidad = Oportunidad(id, actividades, etapa, clientes, prioridad, ingreso, correo)
    oportunidades.append(oportunidad)


def listar_oportunidades():
    return oportunidades

def eliminar_oportunidad(id):
    for oportunidad in oportunidades:
        id_oportunidad = str(oportunidad.id)
        id = str(id)
        if id_oportunidad == id:
            oportunidades.remove(oportunidad)

    i = 0
    for oportunidad in oportunidades:
        i += 1
        oportunidad.id = i

def modificar_oportunidad(request):
    print("Modificar oportunidad")
"""
def modificar_oportunidad(request):
    id = str(request.form.get("id-modificar"))
    nombre = str(request.form.get("nombre-modificar"))
    telefono = str(request.form.get("telefono-modificar"))
    web = str(request.form.get("web-modificar"))
    direccion = str(request.form.get("direccion-modificar"))
    ciudad = str(request.form.get("ciudad-modificar"))
    email = str(request.form.get("email-modificar"))

    cliente = Cliente(id, nombre, telefono, email, web, direccion, ciudad)

    for cliente_existente in clientes:
        if cliente_existente.id == str(cliente.id):
            cliente_existente.nombre = cliente.nombre
            cliente_existente.telefono = cliente.telefono
            cliente_existente.web = cliente.web
            cliente_existente.direccion = cliente.direccion
            cliente_existente.ciudad = cliente.ciudad
            cliente_existente.email = cliente.email
            print("Cliente modificado: "+str(cliente.id))
            break
"""