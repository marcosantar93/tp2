# Aqui se listan los imports
from flask import Flask
from flask import render_template
from flask import request
import linecache
import time
import urllib
import urllib2



app = Flask(__name__)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i

#fo = open('test.txt','w')



# Define la ruta con la que se ingresara desde el browser
freq = 5
@app.route('/', methods = ['GET','POST'])
def index():
    fo = open('freqs.txt', 'r')
    valor = fo.read()
    freq = int(valor)
    fo.close()
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
    linecache.clearcache()

    if request.method == 'POST':
        data = request.form
        freq = data["freq"]
        fo = open('freqs.txt', 'w')
        fo.write(str(freq))
        fo.close()
        return render_template('response.html', freq=freq, tempa=tempa, presa=presa, humea=humea, winda=winda, tempm=tempm, presm=presm, humem=humem, windm=windm)
    if request.method =='GET':
        return render_template('response.html', freq=freq, tempa=tempa, presa=presa, humea=humea, winda=winda, tempm=tempm, presm=presm, humem=humem, windm=windm)


if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=8080)
