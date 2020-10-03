import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def num_primos():

    maximo = 100
    x = 1
    inicio = 3
    primos = "2, "

    while x < maximo:
        p = 1
        for i in range(2, inicio):
            if inicio % i == 0:
                p = 0
        if (p):
            primos = primos + str(inicio) + ", "
            x += 1
            if (x % 10 == 0):
                primos = primos
        inicio += 1
        
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
