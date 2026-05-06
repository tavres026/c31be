from flask import Flask

app = Flask(__name__)

@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return 'Cadeado Aberto'
    else: 
        return 'Cadeado Fechado'

if __name__ == '__main__':
    app.run(debug=True)


def soma(a, b):
    return a + b    
def subtracao(a, b):
    return a - b    
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return 'Erro: Divisão por zero não é permitida.'
    
@app.route('/calculadora/<operacao>/<int:a>/<int:b>')
def calculadora(operacao, a, b):
    if operacao == 'soma':
        resultado = soma(a, b)
    elif operacao == 'subtracao':
        resultado = subtracao(a, b)
    elif operacao == 'multiplicacao':
        resultado = multiplicacao(a, b)
    elif operacao == 'divisao':
        resultado = divisao(a, b)
    else:
        return 'Operação inválida. Use soma, subtracao, multiplicacao ou divisao.'
    
    return f'O resultado da {operacao} entre {a} e {b} é: {resultado}'      