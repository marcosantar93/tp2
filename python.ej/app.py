# Aqui se listan los imports
from flask import Flask
from flask import render_template
from flask import request
import linecache

app = Flask(__name__)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i

#fo = open('test.txt','w')


# Define la ruta con la que se ingresara desde el browser
@app.route('/')
def index():
    currentLine = file_len('test.txt')
    tempm = 0
    presm = 0
    humem = 0
    windm = 0
    for i in range(0, 10):
        line = linecache.getline('test.txt', currentLine - i)
        valores = line.split()
        if i == 0:
            tempa = float(valores[0])
            presa = float(valores[1])
            humea = float(valores[2])
            winda = float(valores[3])
        tempm += float(valores[0])
        presm += float(valores[1])
        humem += float(valores[2])
        windm += float(valores[3])

    tempm /= 10
    presm /= 10
    humem /= 10
    windm /= 10
    return render_template('response.html', tempa=tempa, presa=presa, humea=humea, winda=winda, tempm=tempm, presm=presm, humem=humem, windm=windm)

# Define la ruta y metodo con el que se debe llegar a este endpoint
@app.route('/form', methods = ['POST'])
def action_form():

    if request.method == 'POST':
        data = request.form
        nombre = data["nombre"]
        apellido = data["apellido"]
        email = data["email"]

        if data["sexo"] == "masc":
            sexo = "Masculino"
        else:
            sexo = "Femenino"
        return render_template('response.html', nombre=nombre, apellido=apellido, email=email, sexo=sexo)

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=8080)
