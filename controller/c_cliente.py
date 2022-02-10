from flask import jsonify

from model.cliente import Cliente

clientes = []


# Método que dice cual es el próximo id para generar un nuevo cliente
def getNextId(clientes):
    return len(clientes) + 1

# Método para agregar un nuevo cliente
def anadir_cliente(request):
    id = str(getNextId(clientes))
    nombre = str(request.form.get("nombre"))
    telefono = str(request.form.get("telefono"))
    web = str(request.form.get("web"))
    direccion = str(request.form.get("direccion"))
    ciudad = str(request.form.get("ciudad"))
    email = str(request.form.get("email"))

    cliente = Cliente(id, nombre, telefono, email, web, direccion, ciudad)

    clientes.append(cliente)


def listar_clientes():
    return clientes

def eliminar_cliente():
    for cliente in clientes:
        if cliente.id == id:
            clientes.remove(cliente)
            return "Cliente eliminado"
    return "No se encontró el cliente"

def modificar_cliente():
    print("modificar clientes")
