from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    #어떤 정보를 리퀘스트해서 포스트할지 정리
    #여기선 제목/작가이름/리뷰내용을 받음
    recieve_title = request.form['give_title']
    recieve_author = request.form['give_author']
    recieve_review = request.form['give_review']
    #받는 정보들을 딕셔너리 형태로 정렬
    review = {'title':recieve_title,'author':recieve_author,'review':recieve_review}
    #db에 받은 정보들 삽입
    db.reviews.insert_one(review)
    return jsonify({'result':'success', 'msg': '리뷰 작성이 완료되었습니다! :)'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({},{'_id':0}))
    return jsonify({'result':'success', 'reviews':reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)