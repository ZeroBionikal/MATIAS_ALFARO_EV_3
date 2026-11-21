from flask import Flask, request, render_template

app = Flask(__name__)


# Funciones para el Ejercicio 1
def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def obtener_estado(promedio, asistencia):
    # Se deben cumplir dos condiciones para aproba
    if promedio >= 40 and asistencia >= 75:
        return "APROBADO"
    else:
        return "REPROBADO"


# Funcion para el Ejercicio 2
def nombre_mas_largo(nombres):
    mayor = nombres[0]
    for nombre in nombres:
        if len(nombre) > len(mayor):
            mayor = nombre
    return mayor


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    # Variables que se envian a la plantilla
    nota1 = ""
    nota2 = ""
    nota3 = ""
    asistencia = ""
    promedio = None
    estado = None
    error = None

    if request.method == 'POST':
        # Se recogen los datos del formulario
        nota1 = request.form['nota1']
        nota2 = request.form['nota2']
        nota3 = request.form['nota3']
        asistencia = request.form['asistencia']

        try:
            n1 = float(nota1)
            n2 = float(nota2)
            n3 = float(nota3)
            asis = float(asistencia)

            if n1 < 10 or n1 > 70 or n2 < 10 or n2 > 70 or n3 < 10 or n3 > 70:
                error = "Las notas deben estar entre 10 y 70."
            elif asis < 0 or asis > 100:
                error = "La asistencia debe ser entre 0 y 100."
            else:
                promedio = round(calcular_promedio(n1, n2, n3), 1)
                estado = obtener_estado(promedio, asis)
        except ValueError:
            error = "Debes ingresar solo numeros en todos los campos."

    return render_template('ejercicio1.html',
                           nota1=nota1, nota2=nota2, nota3=nota3,
                           asistencia=asistencia, promedio=promedio,
                           estado=estado, error=error)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre1 = ""
    nombre2 = ""
    nombre3 = ""
    mayor = None
    cantidad = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        mayor = nombre_mas_largo(nombres)
        cantidad = len(mayor)

    return render_template('ejercicio2.html',
                           nombre1=nombre1, nombre2=nombre2, nombre3=nombre3,
                           mayor=mayor, cantidad=cantidad)


if __name__ == '__main__':
    app.run(debug=True)