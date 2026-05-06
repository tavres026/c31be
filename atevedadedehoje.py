from flask import Flask

app = Flask(__name__)

@app.route('/ola/<nome>')
def saudacao(nome):
    return f'Olá, {nome}! Bem-vindo ao Flask!'

@app.route('/calcular/<operacao>/<int:a>/<int:b>')
def calcular(operacao, a, b):
    soma = a + b
    return f'O resultado da {operacao} entre {a} e {b} é: {soma}'

@app.route('/idade/nome/<nome>/idade/<int:idade>')
def idade(nome, idade):
    if idade < 18:
        return f'{nome}, você é menor de idade.'
    else:
        return f'{nome}, você é maior de idade.'
    
@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f'O produto {nome} custa R${preco:.2f}.'

@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    resultado = palavra * vezes
    return f'A palavra "{palavra}" repetida {vezes} vezes é: {resultado}'   

if __name__ == '__main__':
    app.run(debug=True)    