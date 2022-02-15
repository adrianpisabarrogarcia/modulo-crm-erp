# libraries
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from gapminder import gapminder

def generar_graficos():
    data = {
        "cantidad_oportunidades": cantidad_oportunidades()
    }


# guardar el gráfico y devolver la ruta en la que esta guardado
def generar_archivo():
    nombre_fichero = str(datetime.datetime.now()).replace(':', '-').replace('.', '-').replace(' ', '-')
    ruta = "./static/img/"
    extension = ".png"
    enlace_completo = ruta + nombre_fichero + extension
    #guardar fichero
    plt.savefig(enlace_completo)
    plt.show()
    #devolver la ruta
    return str(enlace_completo)

def cantidad_oportunidades():
    # data
    data = gapminder.loc[gapminder.year == 2007]
    # use the scatterplot function to build the bubble map
    sns.scatterplot(data=data, x="prueba-x", y="prueba-y", size="pop", legend=False, sizes=(20, 2000))
    return generar_archivo()

