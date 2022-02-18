from model.actividad import Actividad

actividades = []

# Método que dice cual es el próximo id para generar una mueva actividad
def getNextId():
    return len(actividades) + 1

# Método para agregar una nueva activiadad
def anadir_actividad(request):
    id = str(getNextId())
    descripcion = str(request.form.get("descripcion"))
    fecha_vencimiento = str(request.form.get("fecha-vencimiento"))
    fecha_limite = str(request.form.get("fecha-limite"))
    resumen = str(request.form.get("resumen"))
    tipo = str(request.form.get("tipo"))

    actividad = Actividad(id, descripcion, fecha_vencimiento, fecha_limite, resumen, tipo)
    actividades.append(actividad)

def listar_actividades():
    return actividades

def eliminar_actividades(id):
    for actividad in actividades:
        id_actividad = str(actividad.id)
        id = str(id)
        if id_actividad == id:
            actividades.remove(actividad)

    i = 0
    for actividad in actividades:
        i += 1
        actividad.id = i

def modificar_actividad(request):
    id = str(request.form.get("id-modificar"))
    descripcion = str(request.form.get("descripcion-modificar"))
    fecha_vencimiento = str(request.form.get("fecha-vencimiento-modificar"))
    fecha_limite = str(request.form.get("fecha-limite-modificar"))
    resumen = str(request.form.get("resumen-modificar"))
    tipo = str(request.form.get("tipo-modificar"))

    actividad = Actividad(id, descripcion, fecha_vencimiento, fecha_limite, resumen, tipo)

    for actividad_existente in actividades:
        if actividad_existente.id == str(actividad.id):
            actividad_existente.descripcion = str(actividad.descripcion)
            actividad_existente.fecha_vencimiento = str(actividad.fecha_vencimiento)
            actividad_existente.fecha_limite = str(actividad.fecha_limite)
            actividad_existente.resumen = str(actividad.resumen)
            actividad_existente.tipo = str(actividad.tipo)
            break
