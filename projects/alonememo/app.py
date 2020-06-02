#순서
# post 서버 - html 연결(url/comment정보를 가지고 url내의 meta태그 크롤링)
# get 서버 - html 연결
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
  reviewing = list(db.reviewing.find({}, {'_id':0}))
  return jsonify({'result':'success', 'reviewing':reviewing})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
  recieve_url = request.form['give_url']
  recieve_comment = request.form['give_comment']

  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(recieve_url,headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')

  og_image = soup.select_one('meta[property="og:image"]')
  og_title = soup.select_one('meta[property="og:title"]')
  og_desc = soup.select_one('meta[property="og:description"]')

  image = og_image['content']
  title = og_title['content']
  desc = og_desc['content'] #왜 이게 null값으로 되어있을까???

  movie = {
    'image':image,
    'title':title,
    'url':recieve_url,
    'desc':desc,
    'comment':recieve_comment
  }

  db.reviewing.insert_one(movie)
  return jsonify({'result': 'success', 'msg':'리뷰가 등록되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)