from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from controller.c_cliente import anadir_cliente, listar_clientes, eliminar_cliente, modificar_cliente

app = Flask(__name__)

########################################################################################################################
# Oportunidades: Mostrar
@app.route('/')
def home():
    request.args.get('page')
    return render_template('oportunidades.html')


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
def delete_clintes():
    if request.method == "GET":
        id = str(request.args.get("id"))
        print(id)
        eliminar_cliente(id)
    return redirect(url_for('clientes'))

########################################################################################################################
# Informes: Mostrar
@app.route('/informes')
def informes():
    return render_template('informes.html')





if __name__ == '__main__':
    app.run(debug=True)