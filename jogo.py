from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    variavel = 'Jogo: Adivinhe o número de 1 a 10!'

    if request.method == 'GET':
       return render_template("index.html", variavel=variavel)
    else:
        numero = randint(1,10)
        palpite = int(request.form.get('name'))

        if numero == palpite:
            return '<h1>Você acertou!</h1>'
        else:
            return '<h1>Você perdeu!</h1>'


@app.route('/<string:nome>')
def error(nome):
    variavel = f'A página ({nome}) não existe!'
    return render_template('error.html', variavel2=variavel )    

if __name__ == "__main__":
    app.run(debug=True)    