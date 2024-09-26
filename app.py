from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/media_notas')
def media_notas():
    return render_template('media_notas.html')

@app.route('/calculadora_simples')
def calculadora_simples():
    return render_template('calculadora_simples.html')

@app.route('/imc_valor')
def imc_valor():
    return render_template('imc_valor.html')

if __name__=='__main__':
    app.run()