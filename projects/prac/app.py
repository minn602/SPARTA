from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/') #url+/를 주소창에 입력하게 되면 home() 함수가 실행된다
def home():
   return render_template('index.html')

@app.route('/test', method=['POST'])
def test_post:
   title_recieve = request.form['title_give']
   print(title_recieve)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)