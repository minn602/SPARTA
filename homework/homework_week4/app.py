from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods = ['POST'])
def save_orderinfo():
    recieve_name = request.form['give_name']
    recieve_qty = request.form['give_qty']
    recieve_address = request.form['give_address']
    recieve_phone = request.form['give_phone']

    order = {
    'name' : recieve_name,
    'qty' : recieve_qty,
    'address' : recieve_address,
    'phone' : recieve_phone
    }
    db.orders.insert_one(order)

    return jsonify({'result':'success', 'msg':'주문이 완료되었습니다!'})

@app.route('/test', methods = ['GET'])
def read_orderinfo():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders':orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)