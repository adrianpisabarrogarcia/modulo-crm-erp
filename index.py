from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('oportunidades.html')

@app.route('/etapas')
def etapas():
    return render_template('etapas.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/informes')
def informes():
    return render_template('informes.html')

if __name__ == '__main__':
    app.run(debug=True)