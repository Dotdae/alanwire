from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Con'

@app.route('/mm', methods=['POST'])
def getMaximax():

    if(len(request.json) <= 0):

        message = {'data': 'No se enviaron datos'}

    else:

        # Turn data to json

        data = request.json

        # Extract and process the keys in single values

        keys = data.keys()
        values = data.values()
        
        keyList = list()

        for key in keys:
            keyList.append(key)

        # Extract and process the value in single items

        valueList = list()

        for value in values:
            valueList.append(value)

        
        max = valueList[0]
        ind = 0

        for i in range(len(valueList)):
            if(max < valueList[i]):
                max = valueList[i]
                ind = i

        

        message = {keyList[ind]: max}


    return jsonify(message)

@app.route('/rs', methods=['POST'])
def getCoeficienteOptimismo():
     
    p = 0.6 
    q = 1 - p

    data = request.json
    d = list()
    out = {}

    for i in range(len(data)):
        d.append(data[i])
        keys = d[i].keys()
        values = d[i].values()
        values = getValues(values)
        keys = getKeys(keys)

        # Crea un diccionario con los resultados, el diccionario está al revés
        # el primer elemento, en este caso tv, será el último en salir y el último
        # en entrar será el primero

        out[keys[0] + " salida"] =  p * values[1] + q * values[2]

    return out

@app.route('/lp', methods=['POST'])
def getLaplace():
    pass

    data = request.json
    d = list()
    out = {}

    for i in range(len(data)):
        d.append(data[i])
        keys = d[i].keys()
        values = d[i].values()
        values = getValues(values)
        keys = getKeys(keys)

        # Crea un diccionario con los resultados, el diccionario está al revés
        # el primer elemento, en este caso tv, será el último en salir y el último
        # en entrar será el primero

        out[keys[0] + " salida"] =  round((values[1] + values[2] + values[3]) / 3, 2)

    print(out)

    return out

@app.route('/minm', methods=['POST'])
def getMinimax():

    data = request.json

    d = list()
    out = {}
    nums = []


    for i in range(len(data)):
        d.append(data[i])
        
        values = d[i].values()
        values = getValues(values)
        
        # Toma los 3 valores de cada item.

        n = [values[1], values[2], values[3]]

        # Se guardan en sublistas

        nums.append(n)

    # Se extraen los datos de cada columna y se guardan en una lista
    # después se manda a una función para determinar cuál es el mayor.

    for i in range(3):

        lst2 = [item[i] for item in nums]
        h = isHigher(lst2)

    return out

# Funciones para manejar diccionarios.

def getKeys(data):

    keyList = list()

    for key in data:
        keyList.append(key)
    
    return keyList

def getValues(data):
    
    valueList = list()

    for value in data:
        valueList.append(value)
    
    return valueList
    
def isHigher(nums):
    

    h = max(nums, key=int)

    return h

if __name__ == '__main__':
    app.run(debug=True)