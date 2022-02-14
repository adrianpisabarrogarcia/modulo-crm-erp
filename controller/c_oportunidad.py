from model.oportunidad import Oportunidad
from controller.c_actividad import actividades
from controller.c_cliente import clientes

oportunidades = []

# Método que dice cual es el próximo id para generar una nueva oportunidad
def getNextId():
    return len(oportunidades) + 1

# Método para agregar una nueva oportunidad
def anadir_oportunidad(request):
    id = str(getNextId())
    imput_actividades = str(request.form.get("actividades"))
    etapa = str(request.form.get("etapa"))
    imput_clientes = str(request.form.get("clientes"))
    prioridad = str(request.form.get("prioridad"))
    ingreso = str(request.form.get("ingreso"))

    print("id: " + id)
    print("actividades: " + imput_actividades)
    print("etapa: " + etapa)
    print("clientes: " + imput_clientes)
    print("prioridad: " + prioridad)
    print("ingreso: " + ingreso)


    # introducir actividades en una lista de actividades para después agregarlas a la oportunidad creada
    listado_actividades = []
    split_actividades = imput_actividades.split(",")
    for split_id in split_actividades:
        for actividad in actividades:
            if str(actividad.id) == split_id:
                listado_actividades.append(actividad)
                break

    # introducir clientes en una lista de clientes para después agregarlas a la oportunidad creada
    listado_clientes = []
    split_clientes = imput_clientes.split(",")
    for split_id in split_clientes:
        for cliente in clientes:
            if str(cliente.id) == split_id:
                listado_clientes.append(cliente)
                break

    oportunidad = Oportunidad(id, listado_actividades, etapa, listado_clientes, prioridad, ingreso)
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