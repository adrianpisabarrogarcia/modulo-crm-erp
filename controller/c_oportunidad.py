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
    input_actividades = str(request.form.get("actividades"))
    etapa = str(request.form.get("etapa"))
    input_clientes = str(request.form.get("clientes"))
    prioridad = str(request.form.get("prioridad"))
    ingreso = str(request.form.get("ingreso"))


    # introducir actividades en una lista de actividades para después agregarlas a la oportunidad creada
    listado_actividades = devolver_actividades_clientes_concrectos(input_actividades, "actividades")

    # introducir clientes en una lista de clientes para después agregarlas a la oportunidad creada
    listado_clientes = devolver_actividades_clientes_concrectos(input_clientes, "clientes")

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
            volver_a_definir_ids()
            break



def modificar_oportunidad(request):
    id = str(request.form.get("id"))
    input_actividades = str(request.form.get("actividades"))
    etapa = str(request.form.get("etapa"))
    input_clientes = str(request.form.get("clientes"))
    prioridad = str(request.form.get("prioridad"))
    ingreso = str(request.form.get("ingreso"))


    # introducir actividades en una lista de actividades para después agregarlas a la oportunidad creada
    listado_actividades = devolver_actividades_clientes_concrectos(input_actividades, "actividades")

    # introducir clientes en una lista de clientes para después agregarlas a la oportunidad creada
    listado_clientes = devolver_actividades_clientes_concrectos(input_clientes, "clientes")

    oportunidad = Oportunidad(id, listado_actividades, etapa, listado_clientes, prioridad, ingreso)
    print(oportunidad)
    for oportunidad_existente in oportunidades:
        if str(oportunidad_existente.id) == str(id):
            oportunidades.remove(oportunidad_existente)
            oportunidades.append(oportunidad)
            volver_a_definir_ids()
            print("Modificado")
            break

def devolver_actividades_clientes_concrectos(input, tipo):
    listado = []
    split = input.split(",")

    if tipo == "actividades":
        for id in split:
            for actividad in actividades:
                if str(actividad.id) == id:
                    listado.append(actividad)
                    break
    elif tipo == "clientes":
        for id in split:
            for cliente in clientes:
                if str(cliente.id) == id:
                    listado.append(cliente)
                    break
    return listado

def volver_a_definir_ids():
    i = 0
    for oportunidad in oportunidades:
        i += 1
        oportunidad.id = i
