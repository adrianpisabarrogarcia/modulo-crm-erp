from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from controller.c_cliente import anadir_cliente, listar_clientes, eliminar_cliente, modificar_cliente

app = Flask(__name__)

@app.route('/')
def home():
    request.args.get('page')
    return render_template('oportunidades.html')

@app.route('/clientes', methods=["GET", "POST"])
def clientes():
    clientes = listar_clientes()
    if request.method == "POST":
        anadir_cliente(request)

    return render_template('clientes.html', clientes=clientes)

@app.route('/informes')
def informes():
    return render_template('informes.html')

if __name__ == '__main__':
    app.run(debug=True)