# libraries
import datetime
import os
from sys import platform

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

from controller.c_oportunidad import num_oportunidades_en_cada_etapa, num_oportunidades_en_cada_ingreso, \
    num_oportunidades_en_cada_prioridad
import numpy as np
import pathlib



def generar_graficos():
    datos = {
        "etapas": cantidad_oportunidades(),
        "prioridades": cantidad_oportunidades_por_prioridad(),
        "ingresos": cantidad_oportunidades_por_ingreso(),

    }

    return datos


# guardar el gráfico y devolver la ruta en la que esta guardado
def generar_archivo(veces1):
    nombre_fichero = str(datetime.datetime.now()).replace(':', '-').replace('.', '-').replace(' ', '-')
    extension = ".png"
    sistemaoperativo = str(os.name)
    print("so: " + sistemaoperativo)
    if sistemaoperativo == "linux" or sistemaoperativo == "linux2" or sistemaoperativo == "darwin":
        #para so basado en linux, mac os
        ruta = str(pathlib.Path().absolute()) + "/static/img/grafico"
    else:
        #para windows
        ruta = str(pathlib.Path().absolute()) + "\\static\\img\\grafico"
    # guardar fichero
    # plt.show()
    enlace_completo = ruta + nombre_fichero + extension
    plt.savefig(enlace_completo)
    plt.close()

    nombre_fichero = "grafico" + nombre_fichero


    # devolver la ruta
    return str(nombre_fichero + extension)


def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def cantidad_oportunidades():
    # create data
    data = num_oportunidades_en_cada_etapa()

    try:
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        data = [data["nuevo"], data["calificado"], data["propuesta"], data["ganada"]]
        ingredients = ['Nuevo', 'Calificado', 'Propuesta', 'Ganada']

        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))
        ax.legend(wedges, ingredients,
                  title="Oportunidades",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title("Etapas de las oportunidades")


    except:
        return "Error"
    return generar_archivo(1)


def cantidad_oportunidades_por_prioridad():
    # create data
    data = num_oportunidades_en_cada_prioridad()

    try:

        # create a dataset
        height = [data["alta"], data["media"], data["baja"]]
        bars = ("Alta", "Media", "Baja")

        x_pos = np.arange(len(bars))

        # Create bars
        plt.bar(x_pos, height, color=(0.2, 0.4, 0.6, 0.6))

        # Create names on the x-axis
        plt.xticks(x_pos, bars)

        # Show graph
        # plt.show()

    except:
        return "Error"

    return generar_archivo(2)


def cantidad_oportunidades_por_ingreso():
    # create data
    data = num_oportunidades_en_cada_ingreso()

    height = []
    bars = ()

    for i in range(len(data)):
        height.append(data[i]["ingreso"])
        bars = bars + (data[i]["id"],)

    y_pos = np.arange(len(bars))

    # Create bars
    plt.barh(y_pos, height)

    # Create names on the x-axis
    plt.yticks(y_pos, bars)

    return generar_archivo(3)
