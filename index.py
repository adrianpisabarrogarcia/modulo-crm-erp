from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from controller.c_cliente import anadir_cliente, listar_clientes, eliminar_cliente, modificar_cliente
from controller.c_oportunidad import anadir_oportunidad, listar_oportunidades, eliminar_oportunidad, modificar_oportunidad, listar_oportunidad
from controller.c_actividad import anadir_actividad, listar_actividades, eliminar_actividades, modificar_actividad
from controller.c_informes import generar_graficos

app = Flask(__name__)

########################################################################################################################
# Oportunidades: Mostrar y Añadir
@app.route('/', methods=["GET", "POST"])
def home():
    oportunidades = listar_oportunidades()
    actividades = listar_actividades()
    clientes = listar_clientes()
    if request.method == "POST":
        anadir_oportunidad(request)

    return render_template('oportunidades.html', oportunidades=oportunidades, actividades=actividades, clientes=clientes)

# Oportunidades: Eliminar
@app.route('/oportunidades/delete')
def delete_oportunidad():
    if request.method == "GET":
        id = str(request.args.get("id"))
        eliminar_oportunidad(id)
    return redirect(url_for('home'))

# Oportunidades: Modificar
@app.route('/oportunidades/edit', methods=["GET", "POST"])
def edit_oportunidad():
    if request.method == "GET":
        id = str(request.args.get("id"))
        oportunidad = listar_oportunidad(id)
        actividades = listar_actividades()
        clientes = listar_clientes()
        #mostrar pagina de modificar una oportunidad
        return render_template('edit-oportunidades.html', oportunidad=oportunidad, actividades=actividades, clientes=clientes)
    else:
        modificar_oportunidad(request)
    return redirect(url_for('home'))


########################################################################################################################
# Clientes: Mostrar y Añadir
@app.route('/clientes', methods=["GET", "POST"])
def clientes():
    clientes = listar_clientes()
    if request.method == "POST":
        anadir_cliente(request)

    return render_template('clientes.html', clientes=clientes)

# Clientes: Modificar
@app.route('/clientes/edit', methods=["GET", "POST"])
def edit_clientes():
    if request.method == "POST":
        modificar_cliente(request)

    return redirect(url_for('clientes'))

# Clientes: Eliminar
@app.route('/clientes/delete')
def delete_clientes():
    if request.method == "GET":
        id = str(request.args.get("id"))
        eliminar_cliente(id)
    return redirect(url_for('clientes'))

#########################################################################################################################
# Actividades: Mostrar y Añadir
@app.route('/actividades', methods=["GET", "POST"])
def actividades():
    actividades = listar_actividades()
    if request.method == "POST":
        anadir_actividad(request)

    return render_template('actividades.html', actividades=actividades)

# Actividades: Modificar
@app.route('/actividades/edit', methods=["GET", "POST"])
def edit_actividades():
    if request.method == "POST":
        modificar_actividad(request)

    return redirect(url_for('actividades'))

# Actividades: Eliminar
@app.route('/actividades/delete')
def delete_actividades():
    if request.method == "GET":
        id = str(request.args.get("id"))
        eliminar_actividades(id)
    return redirect(url_for('actividades'))

########################################################################################################################
# Informes: Mostrar
@app.route('/informes')
def informes():
    generar_graficos()
    return render_template('informes.html')





if __name__ == '__main__':
    app.run(debug=True)