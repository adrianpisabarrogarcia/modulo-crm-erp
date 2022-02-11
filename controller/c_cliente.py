from model.cliente import Cliente

clientes = []


# Método que dice cual es el próximo id para generar un nuevo cliente
def getNextId():
    return len(clientes) + 1

# Método para agregar un nuevo cliente
def anadir_cliente(request):
    id = str(getNextId())
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

def eliminar_cliente(id):
    for cliente in clientes:
        id_cliente = str(cliente.id)
        id = str(id)
        if id_cliente == id:
            clientes.remove(cliente)

    i = 0
    for cliente in clientes:
        i += 1
        cliente.id = i


def modificar_cliente(request):
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
