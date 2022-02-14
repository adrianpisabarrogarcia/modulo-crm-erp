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

def listar_oportunidad(id):
    for oportunidad in oportunidades:
        if str(oportunidad.id) == str(id):
            return oportunidad
    return None

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
    print("modificar_oportunidad")
    """
    id = str(getNextId())
    imput_actividades = str(request.form.get("actividades"))
    etapa = str(request.form.get("etapa"))
    imput_clientes = str(request.form.get("clientes"))
    prioridad = str(request.form.get("prioridad"))
    ingreso = str(request.form.get("ingreso"))


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
    """
