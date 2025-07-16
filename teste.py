from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Fila de pedidos e controle de estado
orders = []
current_order = None

# Função para adicionar um pedido à fila
def add_order(name, items):
    number = len(orders) + 1
    order_details = f"Pedido {number}: {name} - Itens: {items}"
    orders.append(order_details)
    return order_details

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/display')
def display():
    return render_template('display.html')

# Rota para fazer um pedido com nome e itens
@app.route('/order/<name>', methods=['POST'])
def order(name):
    data = request.get_json()

    items = []
    if data.get('xBurguer', 0) > 0:
        items.append(f"X-Burguer (Quantidade: {data['xBurguer']})")
    if data.get('xSalada', 0) > 0:
        items.append(f"X-Salada (Quantidade: {data['xSalada']})")
    if data.get('batata', 0) > 0:
        items.append(f"Batata Frita (Quantidade: {data['batata']})")
    if data.get('refrigerante', 0) > 0:
        items.append(f"Refrigerante (Quantidade: {data['refrigerante']})")

    order = add_order(name, ', '.join(items))
    return jsonify({"order": order})

@app.route('/orders')
def get_orders():
    return jsonify({"orders": orders})

@app.route('/next')
def next_order():
    global current_order
    if orders:
        current_order = orders.pop(0)
    else:
        current_order = None
    return jsonify({"current_order": current_order})

@app.route('/current')
def current():
    return jsonify({"current_ticket": current_order})

if __name__ == '__main__':
    app.run(debug=True)

